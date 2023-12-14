from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
INPUT = f"../input/test{DAY}.txt"

A = 0
B = 0

data = []
for line in lines(INPUT):
    data.append(list(line))


def iterate_north(data):
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


def iterate_south(data):
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


def iterate_east(data):
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


def iterate_west(data):
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


def cycle(data):
    changed = 0
    changed += iterate_north(data)
    changed += iterate_west(data)
    changed += iterate_south(data)
    changed += iterate_east(data)
    return changed


cycle(data)
dump_2d(data)

height = len(data)
for y, row in enumerate(data):
    for x, ch in enumerate(row):
        if ch == 'O':
            A += height - y


print("A:", A)
print("B:", B)
