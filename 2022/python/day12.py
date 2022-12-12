from std import *

DAY = "12"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

field = []
start = (-1, -1)
goal = (-1, -1)

row = 0
for line in lines(INPUT):
    if 'S' in line:
        start = (line.index('S'), row)
    if 'E' in line:
        goal = (line.index('E'), row)

    field.append(line)
    row += 1


def get(field, x, y):
    return field[y][x]


def get_height(field, x, y):
    ch = get(field, x, y)
    if ch == 'S':
        return 0
    if ch == 'E':
        return 26
    return ord(ch) - ord('a')


def dump(field, visited):
    for y in range(len(field)):
        line = field[y]
        for x in range(len(line)):
            if (x,y) in visited:
                print("#", end='')
            else:
                print(line[x], end='')
        print()


def crawl_fewest(field, start, goal):
    H = len(field)
    W = len(field[0])

    visited = set()
    explore = set()
    explore.add(start)

    for round in range(10000):
        points = explore
        explore = set()

        for p in points:
            active_height = get_height(field, *p)
            for np in tdlr_2d(p[0], p[1], W, H):
                if np in visited:
                    continue
                height = get_height(field, *np)
                if active_height + 1 < height:
                    continue
                if get(field, *np) == 'E':
                    return round + 1
                visited.add(np)
                explore.add(np)
    return -1


print("A:", crawl_fewest(field, start, goal))


def get_a(field):
    row = 0
    for line in field:
        col = 0
        for ch in line:
            if ch == 'a':
                yield col, row
            col += 1
        row += 1


min_steps = 10000

for a_pos in get_a(field):
    steps = crawl_fewest(field, a_pos, goal)
    if steps <= 0:
        continue
    min_steps = min(min_steps, steps)

print("B:", min_steps)
