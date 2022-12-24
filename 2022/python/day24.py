from collections import deque

from std import *
import copy
import re
import functools
import itertools

DAY = "24"
INPUT = f"../input/input{DAY}.txt"
#INPUT = "../input/test.txt"

DIR = {'<': Vec2(-1, 0), '>': Vec2(1, 0), 'v': Vec2(0, 1), '^': Vec2(0, -1)}

data, h, w = load_2d(INPUT)
start = Vec2(1, 0)
goal = Vec2(w - 2, h - 1)
bliz = []
for y, line in enumerate(data):
    for x, ch in enumerate(line):
        if ch == '#' or ch == '.':
            continue
        data[y][x] = '.'
        bliz.append([Vec2(x, y), DIR[ch]])


def move_bliz(loc):
    positions = set()
    for b in loc:
        b[0] += b[1]
        if b[0].x < 1:
            b[0].x = w - 2
        elif b[0].x > w - 2:
            b[0].x = 1
        elif b[0].y < 1:
            b[0].y = h - 2
        elif b[0].y > h - 2:
            b[0].y = 1
        positions.add(b[0])
    return positions


def dump(field, pos):
    pos = {k[0] for k in pos}
    for y in range(0, h):
        for x in range(0, w):
            ch = field[y][x]
            if Vec2(x, y) in pos:
                ch = 'B'
            print(ch, end='')
        print('')


def part_a():
    points = set()
    points.add(start)

    i = 1
    while points:
        explore = set()
        p_set = move_bliz(bliz)
        for pos in points:
            for nx, ny in tdlr_2d(pos.x, pos.y, w, h, include_center=True):
                n = Vec2(nx, ny)
                if n in p_set or data[n.y][n.x] == '#':
                    continue
                explore.add(n)
        if goal in explore:
            return i
        points = explore
        i += 1
    print("FAIL")
    return -1


A = part_a()
start, goal = goal, start
B1 = part_a()
start, goal = goal, start
B2 = part_a()

print("A:", A)
print("B:", A + B1 + B2)
