pub fn run() {
    println!("=== Day 06 ===");

    let input = include_str!("../../input/input6.txt");

    let part_a = input.split("\n\n").map(|group| {
        group.bytes()
            .filter(|x| x != &b'\n')
            .map(|x| 1 << (x - b'a') as u32)
            .fold(0, |a, x| a | x as u32)
            .count_ones()
    }
    ).sum::<u32>();

    let part_b = input.split("\n\n").map(|group| {
        group.lines()
            .map(|line| {
                line.bytes()
                    .map(|x| 1 << (x - b'a') as u32)
                    .fold(0, |a, x| a | x as u32)
            })
            .fold(0xffffffff, |a, x| a & x)
            .count_ones()
    }).sum::<u32>();

    println!("A: {}", part_a);
    println!("B: {}", part_b);
}
