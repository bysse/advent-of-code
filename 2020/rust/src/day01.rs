pub fn run() {
    println!("=== Day 01 ===");
    let mut numbers: Vec<i32> = include_str!("../../input/input1.txt")
        .lines()
        .map(|x| x.parse::<i32>().unwrap())
        .collect::<Vec<i32>>();

    numbers.sort();

    'outerA: for a in &numbers {
        for b in &numbers {
            if a + b > 2020 {
                break;
            }
            if a + b == 2020 {
                println!("A: {}", a * b);
                break 'outerA;
            }
        }
    }

    'outerB: for a in &numbers {
        for b in &numbers {
            for c in &numbers {
                if a + b + c > 2020 {
                    break;
                }
                if a + b + c == 2020 {
                    println!("B: {}", a * b * c);
                    break 'outerB;
                }
            }
        }
    }
}
