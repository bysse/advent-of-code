import collections

from std import *

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test{DAY}.txt"

pipes = {
    '|': [(0, 1), (0, -1)],
    '-': [(1, 0), (-1, 0)],
    'L': [(1, 0), (0, -1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(-1, 0), (0, 1)],
    'F': [(1, 0), (0, 1)],
}

big_pipes = {
    '|': ['.', '|', '.', '.', '|', '.', '.', '|', '.'],
    '-': ['.', '.', '.', '-', '-', '-', '.', '.', '.'],
    'L': ['.', '|', '.', '.', 'L', '-', '.', '.', '.'],
    'J': ['.', '|', '.', '-', 'J', '.', '.', '.', '.'],
    '7': ['.', '.', '.', '-', '7', '.', '.', '|', '.'],
    'F': ['.', '.', '.', '.', 'F', '-', '.', '|', '.'],
    'S': ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
}

A = 0
B = 0

field = {}
points = set()
y = 0
width = 0
height = 0
start = None
for line in lines(INPUT):
    for x, ch in enumerate(line.strip()):
        if ch == '.':
            points.add((x, y))
            continue
        if ch == 'S':
            start = (x, y)
        field[(x, y)] = ch
        width = max(width, x)
    y += 1
height = y


def trace(pos):
    p0 = pos
    visited = {pos}
    path = [pos]
    length = 1
    while pos in field:
        pipe = field[pos]
        if pipe == 'S':
            break

        for dx, dy in pipes[pipe]:
            new_pos = (pos[0] + dx, pos[1] + dy)
            if new_pos in visited:
                continue
            pos = new_pos
            break

        visited.add(pos)
        path.append(pos)
        if pos == p0:
            break
        length += 1
    return length, visited, path


max_length = 0
max_visited = None
max_position = None
for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    pos = (start[0] + dx, start[1] + dy)
    if pos in field:
        length, visited, positions = trace(pos)
        if length > max_length:
            max_length = length
            max_visited = visited
            max_position = positions

A = int(max_length / 2)


def flood_fill(p0, data):
    q = collections.deque()
    q.append(p0)

    while q:
        p = q.popleft()
        if p[0] < 0 or p[1] < 0:
            continue
        if p[0] >= len(data[0]) or p[1] >= len(data):
            continue
        if data[p[1]][p[0]] != '.':
            continue
        data[p[1]][p[0]] = ' '

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            q.append((p[0] + dx, p[1] + dy))


big = [['.' for _ in range(3 * (width + 1))] for _ in range(3 * (height + 1))]

for x, y, in max_position:
    bp = field[(x, y)]
    i = 0
    for dy in range(3):
        for dx in range(3):
            big[3 * y + dy][3 * x + dx] = big_pipes[bp][i]
            i += 1

flood_fill((0, 0), big)


def count_dots(x, y):
    if 3*y >= len(big) or 3*x >= len(big[0]):
        return 0

    dots = 0
    for dx in range(3):
        for dy in range(3):
            if big[3 * y + dy][3 * x + dx] == '.':
                dots += 1
    return dots

B = 0
for y in range(width):
    for x in range(height):
        dots = count_dots(x, y)
        if dots == 9:
            B += 1

dump_2d(big)

print("A:", A)
print("B:", B)

# 522 too low
# 521 too low
