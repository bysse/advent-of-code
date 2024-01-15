from collections import defaultdict

from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test{DAY}.txt"


def sign(x):
    if x == 0:
        return 0
    return -1 if x < 0 else 1


data = []
for line in lines(INPUT):
    p = ints(line)
    a, b = p[0:3], p[3:]
    points = [tuple(a)]

    while a != b:
        a[0] += sign(b[0] - a[0])
        a[1] += sign(b[1] - a[1])
        a[2] += sign(b[2] - a[2])
        points.append(tuple(a))
    data.append(sorted(points, key=lambda item: item[2]))

data.sort(key=lambda b: b[0][2])

A = 0
B = 0

# height is (height, brick)
height = defaultdict(lambda: (0, -1))


def touches(brick, h_map, dz):
    for (x, y, z) in brick:
        if h_map[(x, y)][0] >= z + dz:
            return True
    return False


supported_by = defaultdict(set)
for n, brick in enumerate(data):
    dz = 0
    while not touches(brick, height, dz):
        dz -= 1
    # commit
    for (x, y, z) in brick:
        (z0, brick_id) = height[(x, y)]
        if z0 == z + dz and brick_id != n:
            supported_by[n].add(brick_id)
        if height[(x, y)][0] < z + dz + 1:
            height[(x, y)] = (z + dz + 1, n)

supports = defaultdict(set)
for brick, below in supported_by.items():
    for b in below:
        supports[b].add(brick)


def can_be_removed(brick_id):
    for id in supports[brick_id]:
        if len(supported_by[id]) == 1:
            return False
    return True


A = 0
for n, brick in enumerate(data):
    if not any(len(supported_by[j]) == 1 for j in supports[n]):
        A += 1

print("A:", A)
print("B:", B)
