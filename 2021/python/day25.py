from std import *
import copy
import re
import functools
import itertools

DAY = "25"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

data, w, h = load2D(INPUT)


def get(data, x, y):
    h = len(data)
    w = len(data[0])
    if x < 0:
        x += w
    if y < 0:
        y += h
    if x >= w:
        x -= w
    if y >= h:
        y -= h
    
    return x, y, data[y][x]

def go(data, herd, dx, dy):
    step = copy.deepcopy(data)

    moves = 0
    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            if ch == herd:
                nx, ny, space = get(data, x+dx, y+dy)
                if space == '.':
                    moves += 1
                    step[y][x] = '.'
                    step[ny][nx] = herd
    return step, moves

def step(data):
    data, m1 = go(data, '>', 1, 0)
    data, m2 = go(data, 'v', 0, 1)
    return data, m1+m2

part_a = 0
for i in range(100000):
    data, moves = step(data)
    if moves == 0:
        part_a = i + 1
        break

print("A:", part_a)
print("B:")