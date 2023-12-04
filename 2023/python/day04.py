import time

from std import *
import copy
import re
import functools
import itertools

DAY = "04"
INPUT = f"../input/input{DAY}.txt"
#INPUT = "../input/test.txt"


def n_winning(a, b):
    c = 0
    for n in a:
        if n in b:
            c += 1
    return c


data = []
for line in lines(INPUT):
    _, card = line.split(':')
    win, ticket = card.split('|')
    data.append((set(ints(win)), set(ints(ticket))))

points = []
matches = []
for win, ticket in data:
    n = n_winning(win, ticket)
    p = 1 << (n - 1) if n > 0 else 0
    points.append(p)
    matches.append(n)

A = sum(points)

t0 = time.time()
for i in range(len(matches) - 1, -1, -1):
    p = matches[i]
    s = 0
    for j in range(0, p):
        idx = i + j + 1
        if idx >= len(matches):
            break
        s += matches[idx]
    matches[i] = s + 1
B = sum(matches)

print("A:", A)
print("B:", B)
