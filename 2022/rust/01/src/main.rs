fn main() {
    let input = include_str!("../input/input.txt");

    let mut calories: Vec<i32> = input.split("\r\n\r\n").map(
        |group| -> i32 {
            group.split("\r\n")
                .filter(|item| item.trim().len() > 0)
                .map(|txt| -> i32 {
                    txt.parse::<i32>().unwrap()
                })
                .sum()
        }
    ).collect();
    calories.sort();
    calories.reverse();

    println!("part1: {}", calories[0]);
    println!("part2: {}", calories[0] + calories[1] + calories[2]);
}
