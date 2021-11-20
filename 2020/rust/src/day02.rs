use regex::Regex;

struct Record {
    a: usize,
    b: usize,
    ch: char,
    s: String
}

pub fn run() {
    println!("=== Day 02 ===");

    let pattern = Regex::new(r#"(\d+)-(\d+) (.): (.+)"#).unwrap();
    let parsed : Vec<Record> = include_str!("../../input/input2.txt")
        .lines()
        .map(|x| pattern.captures(x).unwrap())
        .map(|x| {
            Record {
                a: x[1].parse::<usize>().unwrap(),
                b: x[2].parse::<usize>().unwrap(),
                ch: x[3].as_bytes()[0] as char,
                s: x[4].to_string()
            }
        })
        .collect();

    let count = parsed.iter()
        .filter(|r| {
            let count = r.s.matches(r.ch).count();
            r.a <= count && count <= r.b
        })
        .count();
    println!("A: {}", count);

    let count = parsed.iter()
        .filter(|r| {
            let bytes = r.s.as_bytes();
            let a = bytes[r.a-1] as char;
            let b = bytes[r.b - 1] as char;
            (a == r.ch) as bool ^ (b == r.ch) as bool
        })
        .count();
    println!("B: {}", count);
}