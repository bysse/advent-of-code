from std import *
import copy
import re
import functools
import itertools

DAY = "04"
INPUT = f"../input/input{DAY}.txt"
INPUT = "../input/test.txt"


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
for win, ticket in data:
    n = n_winning(win, ticket)
    p = 1 << (n - 1) if n > 0 else 0
    points.append(p)

A = sum(points)
B = 0

for i in range(len(points) - 1, -1, -1):
    p = points[i]
    s = 0
    for j in range(i, i + p):
        if j >= len(points):
            break
        s += points[j]
    points[i] = s
    print(points)
print(sum(points))

print("A:", A)
print("B:", B)
