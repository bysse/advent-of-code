pub fn run() {
    println!("=== Day 05 ===");

    let mut seat_ids = include_str!("../../input/input5.txt")
        .lines()
        .map(|l| {
            l.chars()
                .map(|x| x as i32)
                .fold(0, |a, x| (a << 1) + ((x % 7) % 2))
        })
        .collect::<Vec<i32>>();

    seat_ids.sort();

    println!("A: {}", seat_ids.get(seat_ids.len() - 1).unwrap());

    let mut p2: i32 = 0;
    let mut p1: i32 = 0;

    for seat_id in seat_ids {
        if seat_id - p2 == 3 {
            println!("B: {}", p1 + 1);
            break;
        }
        p2 = p1;
        p1 = seat_id;
    }
}
