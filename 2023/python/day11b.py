from collections import defaultdict

from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test{DAY}.txt"

data = []
expand = [[], []]
galaxy = []

y = 0
for line in lines(INPUT):
    if line.count(".") == len(line):
        expand[1].append(y)
    data.append(line)
    for x, ch in enumerate(line):
        if ch == ".":
            continue
        galaxy.append((x, y))
    y += 1

for x in range(len(data[0])):
    found = True
    for y in range(len(data)):
        if data[y][x] != ".":
            found = False
            break
    if found:
        expand[0].append(x)


def expand_space(galaxy, expansion):
    expansion -= 1
    for i in range(len(galaxy)):
        ox, oy = x, y = galaxy[i]
        for gx in expand[0]:
            if ox > gx:
                x += expansion
        for gy in expand[1]:
            if oy > gy:
                y += expansion
        galaxy[i] = (x, y)


expand_space(galaxy, 1000000)

B = 0
for i in range(len(galaxy)):
    for j in range(i + 1, len(galaxy)):
        taxi = abs(galaxy[i][0] - galaxy[j][0]) + abs(galaxy[i][1] - galaxy[j][1])
        B += taxi

print("B:", B)
