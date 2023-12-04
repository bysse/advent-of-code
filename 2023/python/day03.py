from collections import defaultdict

from std import *
import copy
import re
import functools
import itertools

DAY = "03"
INPUT = f"../input/input{DAY}.txt"
#INPUT = "../input/test.txt"


def adjacent(x, y):
    yield x - 1, y - 1
    yield x, y - 1
    yield x + 1, y - 1
    yield x - 1, y
    yield x + 1, y
    yield x - 1, y + 1
    yield x, y + 1
    yield x + 1, y + 1


def get_num(line, x):
    x0 = x
    while x < len(line) and ('0' <= line[x] <= '9'):
        x += 1
    return x, int(line[x0:x])


numbers = defaultdict(lambda: set())
symbol = {}
y = 0
for line in lines(INPUT):
    x = -1
    while x+1 < len(line):
        x += 1
        ch = line[x]
        if ch == '.':
            continue
        if '0' <= ch <= '9':
            x2, num = get_num(line, x)
            for tx in range(x, x2):
                for ax, ay in adjacent(tx, y):
                    numbers[(ax, ay)].add(num)
            x = x2-1
            continue
        # this is a symbol
        symbol[(x, y)] = ch
    y += 1

A = 0
B = 0
for pos, symbol in symbol.items():
    if pos in numbers:
        for n in numbers[pos]:
            A += n
    if symbol == '*':
        if pos in numbers:
            nn = numbers[pos]
            if len(nn) == 2:
                nnl = list(nn)
                B += nnl[0] * nnl[1]

print("A:", A)
print("B:", B)
