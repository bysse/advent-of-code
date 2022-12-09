from std import *
import copy
import re
import functools
import itertools

DAY = "09"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

delta = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
}


def add(p, dp):
    return p[0] + dp[0], p[1] + dp[1]


def dir(a, b):
    return -1 if a < b else 1


def sign(x):
    return -1 if x < 0 else 1


data = []
for line in lines(INPUT):
    data.append((delta[line[0]], int(line[1:])))


def move(h, t):
    dd = h[0] - t[0], h[1] - t[1]
    if dd[0] == 0 and abs(dd[1]) >= 2:
        t = add(t, (0, sign(dd[1])))
    elif dd[1] == 0 and abs(dd[0]) >= 2:
        t = add(t, (sign(dd[0]), 0))
    elif abs(dd[0]) > 1 or abs(dd[1]) > 1:
        t = add(t, (sign(dd[0]), sign(dd[1])))
    return t


def simulate(data, knot_count):
    visited = set()
    knots = [(0, 0)] * knot_count

    for dp, steps in data:
        for _ in range(steps):
            knots[0] = add(knots[0], dp)

            for i in range(knot_count-1):
                knots[i+1] = move(knots[i], knots[i+1])

            visited.add(knots[-1])
    return len(visited)


print("A:", simulate(data, 2))
print("B:", simulate(data, 10))
