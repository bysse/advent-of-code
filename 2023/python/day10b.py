from std import *
import copy
import re
import functools
import itertools

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

A = 0
B = 0

field = {}
y = 0
width = 0
height = 0
start = None
for line in lines(INPUT):
    for x, ch in enumerate(line.strip()):
        if ch == '.':
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

inside_points = set()
for i in range(1, len(max_position)):
    p = max_position[i]
    pp = max_position[i-1]
    dx = p[0] - pp[0]
    dy = p[1] - pp[1]
    inside_points.add((p[0] - dy, p[1] + dx))


def flood_fill(p0, max_visited, data=None):
    if p0 in max_visited:
        return 0
    max_visited.add(p0)
    if data:
        data[p0[1]][p0[0]] = '#'
    n = 1
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        p = (p0[0] + dx, p0[1] + dy)
        n += flood_fill(p, max_visited, data)
    return n


B = 0
for p in inside_points:
    if p in max_visited:
        continue
    B += flood_fill(p, max_visited)


print("A:", A)
print("B:", B)

# 522 too low
# 521 too low
