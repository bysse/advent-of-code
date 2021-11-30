use lazy_static::lazy_static;
use regex::Regex;
use std::collections::HashMap;
use std::process;

lazy_static! {
    static ref HCL_PATTERN: Regex = Regex::new(r"^#[0-9a-f]{6}$").unwrap();
    static ref PID_PATTERN: Regex = Regex::new(r"^[0-9]{9}$").unwrap();
}

fn has_all_fields(record: &&HashMap<String, String>) -> bool {
    record.len() >= 7
        && record.len() <= 8
        && record.contains_key("byr")
        && record.contains_key("iyr")
        && record.contains_key("eyr")
        && record.contains_key("hgt")
        && record.contains_key("hcl")
        && record.contains_key("ecl")
        && record.contains_key("pid")
}

fn in_range(x: i32, min: i32, max: i32) -> bool {
    min <= x && x <= max
}

fn if_i32(value: Option<&String>, func: fn(i32) -> bool) -> bool {
    match value {
        Some(n) => match n.parse() {
            Ok(i) => func(i),
            Err(_) => false,
        },
        None => false,
    }
}

fn valid_height(height: &String) -> bool {
    match height.strip_suffix("cm") {
        Some(num) => match num.parse() {
            Ok(n) => in_range(n, 150, 193),
            Err(_) => false,
        },
        None => match height.strip_suffix("in") {
            Some(num) => match num.parse() {
                Ok(n) => in_range(n, 59, 76),
                Err(_) => false,
            },
            None => false,
        },
    }
}

fn has_valid_fields(record: &&&HashMap<String, String>) -> bool {
    if !if_i32(record.get("byr"), |x| in_range(x, 1920, 2002))
        || !if_i32(record.get("iyr"), |x| in_range(x, 2010, 2020))
        || !if_i32(record.get("eyr"), |x| in_range(x, 2020, 2030))
    {
        return false;
    }

    if !valid_height(record.get("hgt").unwrap()) {
        return false;
    }

    if !match record.get("ecl").unwrap().as_ref() {
        "amb" => true,
        "blu" => true,
        "brn" => true,
        "gry" => true,
        "grn" => true,
        "hzl" => true,
        "oth" => true,
        _ => false,
    } {
        return false;
    }

    if !HCL_PATTERN.is_match(record.get("hcl").unwrap()) {
        return false;
    }

    if !PID_PATTERN.is_match(record.get("pid").unwrap()) {
        return false;
    }

    true
}

pub fn run() {
    println!("=== Day 04 ===");

    let mut records: Vec<HashMap<String, String>> = Vec::with_capacity(1000);
    let mut current: HashMap<String, String> = HashMap::with_capacity(10);

    for line in include_str!("../../input/input4.txt").lines() {
        if line.is_empty() {
            records.push(current.clone());
            current.clear();
            continue;
        }

        for field in line.split(" ") {
            let key_value = field.split(":").collect::<Vec<&str>>();
            if key_value.is_empty() || key_value.len() > 2 {
                println!("ERROR: Failed to split {}", field);
                process::exit(1);
            }
            current.insert(String::from(key_value[0]), String::from(key_value[1]));
        }
    }
    if !current.is_empty() {
        records.push(current.clone());
    }

    let has_all_fields = records
        .iter()
        .filter(has_all_fields)
        .collect::<Vec<&HashMap<String, String>>>();
    println!("A: {}", has_all_fields.len());

    println!(
        "B: {}",
        has_all_fields.iter().filter(has_valid_fields).count()
    );
}
