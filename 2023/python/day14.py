from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test{DAY}.txt"

A = 0
B = 0

data = []
for line in lines(INPUT):
    data.append(list(line))


def part_a(data):
    while tilt_north(data) > 0:
        pass
    return weight(data)


def part_b(data):
    for i in range(0, 100):
        cycle(data)
        w = weight(data)
    return w

def cycle(data):
    while tilt_north(data):
        pass
    while tilt_west(data):
        pass
    while tilt_south(data):
        pass
    while tilt_east(data):
        pass


def tilt_north(data):
    changed = 0
    for y in range(1, len(data)):
        target = data[y-1]
        this = data[y]
        for x in range(len(data[0])):
            if this[x] == '.' or this[x] == '#':
                continue
            if target[x] == '.':
                target[x] = 'O'
                this[x] = '.'
                changed += 1
    return changed


def tilt_south(data):
    changed = 0
    for y in range(len(data) - 2, -1, -1):
        target = data[y+1]
        current = data[y]
        for x in range(len(current)):
            if current[x] != 'O':
                continue
            if target[x] == '.':
                target[x] = 'O'
                current[x] = '.'
                changed += 1
    return changed


def tilt_east(data):
    changed = 0
    for line in data:
        for x in range(len(data[0]) - 2, -1, -1):
            if line[x] == '.' or line[x] == '#':
                continue
            if line[x+1] == '.':
                line[x+1] = 'O'
                line[x] = '.'
                changed += 1
    return changed


def tilt_west(data):
    changed = 0
    for line in data:
        for x in range(1, len(data[0])):
            if line[x] != 'O':
                continue
            if line[x-1] == '.':
                line[x-1] = 'O'
                line[x] = '.'
                changed += 1
    return changed


def weight(data):
    w = 0
    height = len(data)
    for y, row in enumerate(data):
        for x, ch in enumerate(row):
            if ch == 'O':
                w += height - y
    return w


print("A:", part_a(copy.deepcopy(data)))
print("B:", part_b(copy.deepcopy(data)))
