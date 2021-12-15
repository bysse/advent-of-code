use std::cmp::Ordering;
use std::collections::{BTreeSet, HashMap};
use std::hash::{Hash, Hasher};

struct Pos {
    x: i32,
    y: i32,
    cost: i32,
}

impl Pos {
    fn new(x: i32, y: i32, cost: i32) -> Self {
        Pos { x, y, cost }
    }
}

impl Eq for Pos {}

impl Ord for Pos {
    fn cmp(&self, other: &Self) -> Ordering {
        self.cost.cmp(&other.cost).then(self.x.cmp(&other.x).then(self.y.cmp(&other.y)))
    }
}

impl PartialEq for Pos {
    fn eq(&self, other: &Self) -> bool {
        self.x == other.x && self.y == other.y
    }
}

impl PartialOrd for Pos {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Hash for Pos {
    fn hash<H: Hasher>(&self, state: &mut H)
        where H: std::hash::Hasher
    {
        state.write_i32(self.x);
        state.write_i32(self.y);
        state.finish();
    }
}


pub fn run() {
    let data = include_str!("../../input/input15.txt");
    //let data = include_str!("../../input/test.txt");

    //let height = data.lines().count();
    //let width = data.lines().map(|line| line.len()).next().unwrap();
    //println!("Size: {}x{}", width, height);

    let field = data
        .chars()
        .filter(|ch| *ch != ' ' && *ch != '\n' && *ch != '\r')
        .map(|ch| ch as i32 - '0' as i32)
        .collect::<Vec<i32>>();

    println!("A: {}", search(&field));

    let field = scale(&field, 5);
    println!("B: {}", search(&field));
}

fn scale(field: &Vec<i32>, scale: usize) -> Vec<i32> {
    let size = (field.len() as f32).sqrt() as usize;
    let n_size = scale * size;

    let mut scaled: Vec<i32> = vec![0; n_size *  n_size]; //Vec::with_capacity((n_size * n_size) as usize);

    for y in 0..size {
        let read = y * size;
        for i in 0..scale {
            let write = read * scale + i * size;

            for j in 0..size {
                let mut value = i as i32 + field[read + j];
                if value > 9 {
                    value -= 9;
                }
                scaled[write + j] = value;
            }
        }
    }

    let chunk = scale * size * size;
    for i in 1..scale {
        let write = i * chunk;
        for j in 0..chunk {
            let mut value= i as i32 + scaled[j];
            if value > 9 {
                value -= 9;
            }
            scaled[write + j] = value;
        }
    }

    return scaled;
}


fn search(field: &Vec<i32>) -> i32 {
    let size = (field.len() as f32).sqrt() as i32;

    let mut frontier: BTreeSet<Pos> = BTreeSet::new();
    let mut visited: HashMap<Pos, i32> = HashMap::new();

    frontier.insert(Pos::new(0, 0, 0));
    visited.insert(Pos::new(0, 0, 0), 0);

    let delta: [(i32, i32); 4] = [(0, -1), (0, 1), (-1, 0), (1, 0)];

    while !frontier.is_empty() {
        let pos = frontier.pop_first().unwrap();

        if pos.x == size - 1 && pos.y == size - 1 {
            return pos.cost;
        }

        for (dx, dy) in delta {
            let x = pos.x + dx;
            let y = pos.y + dy;

            if x < 0 || y < 0 || x >= size || y >= size {
                continue;
            }

            let cost = field[(x + y * size) as usize];
            let total_cost = cost + pos.cost;
            let np = Pos::new(x, y, total_cost);

            match visited.get(&np) {
                Some(previous_cost) => if previous_cost <= &total_cost {
                    continue;
                }
                _ => {}
            }

            frontier.insert(Pos::new(x, y, total_cost));
            visited.insert(np, total_cost);
        }
    }

    return 0;
}