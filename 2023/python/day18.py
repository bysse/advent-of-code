import heapq
from typing import Tuple

from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test{DAY}.txt"

A, B = 0, 0

delta_map = {
    'R': Vec2(1, 0),
    'L': Vec2(-1, 0),
    'U': Vec2(0, -1),
    'D': Vec2(0, 1),
}


def calculate(ops):
    pos = Vec2(0, 0)
    vertices = [pos]
    boundary = 0
    for direction, steps in ops:
        boundary += steps
        pos += steps * delta_map[direction]
        vertices.append(pos)

    S = 0
    for i in range(len(vertices) - 1):
        v1 = vertices[i]
        v2 = vertices[i + 1]
        S += v1.x * v2.y - v1.y * v2.x
    S += boundary
    return (S // 2) + 1


data_a = []
data_b = []
for line in lines(INPUT):
    part = line.split()
    data_a.append((part[0], int(part[1])))

    d = ['R', 'D', 'L', 'U'][int(part[2][7])]
    l = int(part[2][2:7], 16)
    data_b.append((d, l))

print("A:", calculate(data_a))
print("B:", calculate(data_b))
