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

north = {'|', 'L', 'J'}

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
            visited.add(pos)
            path.append(pos)
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
for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    pos = (start[0] + dx, start[1] + dy)
    if pos in field:
        length, visited, _ = trace(pos)
        if length > max_length:
            max_length = length
            max_visited = visited
            if dy == 0:
                if 'S' in north:
                    north.remove('S')
            else:
                north.add('S')

A = int(max_length / 2)
B = 0

for y in range(height):
    outside = False
    for x in range(0, width):
        pos = (x, y)
        if pos in max_visited:
            if field[pos] in north:
                outside = not outside
            continue

        if pos in points and not outside:
            B += 1

print("A:", A)
print("B:", B)
