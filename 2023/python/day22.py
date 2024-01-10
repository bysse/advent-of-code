from collections import defaultdict

from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
INPUT = f"../input/test{DAY}.txt"


def sign(x):
    if x == 0:
        return 0
    return -1 if x < 0 else 1


xy0 = (9999, 9999)
xy1 = (0, 0)

data = []
for line in lines(INPUT):
    p = ints(line)
    a, b = p[0:3], p[3:]
    points = {tuple(a)}
    xy0 = min(xy0, (a[0], a[1]))
    xy1 = max(xy1, (a[0], a[1]))

    while a != b:
        a[0] += sign(b[0] - a[0])
        a[1] += sign(b[1] - a[1])
        a[2] += sign(b[2] - a[2])
        points.add(tuple(a))
        xy0 = min(xy0, (a[0], a[1]))
        xy1 = max(xy1, (a[0], a[1]))
    data.append(points)

A = 0
B = 0

print(f"{xy0} -> {xy1}")
# height is (height, brick)
height = [[(0, -1) for _ in range(xy1[0] - xy0[0] + 1)] for _ in range(xy1[1] - xy0[1] + 1)]


def touches(brick, h_map, dz):
    for (x, y, z) in brick:
        if h_map[y][x][0] >= z + dz:
            return True
    return False


support = defaultdict(set)
for n, brick in enumerate(data):
    dz = 0
    while not touches(brick, height, dz):
        dz -= 1
    # commit
    for (x, y, z) in brick:
        (z0, brick_id) = height[y][x]
        if z0 == z + dz:
            support[n].add(brick_id)
        height[y][x] = (z + dz, n)

for n, brick in enumerate(data):
    for above in range(n, len(data)):
        pass
print(support)

print("A:", A)
print("B:", B)

