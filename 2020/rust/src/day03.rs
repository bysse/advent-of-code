fn ski(field: &Vec<Vec<u8>>, dx: usize, dy: usize) -> i64 {
    let mut x = 0;
    let mut count = 0;

    for row in field.iter().step_by(dy) {
        if row[x] == '#' as u8 {
            count += 1
        }
        x += dx;
        if x >= row.len() {
            x -= row.len();
        }
    }

    return count;
}

pub fn run() {
    println!("=== Day 03 ===");

    let data: Vec<Vec<u8>> = include_str!("../../input/input3.txt")
        .lines()
        .map(|x| x.as_bytes().to_vec())
        .collect();

    let slope0 = ski(&data, 3, 1);
    println!("A: {}", slope0);

    let prod = slope0 * ski(&data, 1, 1) * ski(&data, 5, 1) * ski(&data, 7, 1) * ski(&data, 1, 2);
    println!("B: {}", prod);
}