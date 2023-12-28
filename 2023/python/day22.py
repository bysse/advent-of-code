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
height = [[(0, -1) for _ in range(xy1[0] - xy0[0])] for _ in range(xy1[1] - xy0[1])]
print(height)

# TODO: settle the bricks, one at the time

print("A:", A)
print("B:", B)
