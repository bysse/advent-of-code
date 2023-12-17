from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
INPUT = f"../input/test{DAY}.txt"

data = []
for line in lines(INPUT):
    data.append(ints(line))

data = {}
for y, line in enumerate(lines(INPUT)):
    for x, ch in enumerate(line):
        data[(x, y)] = ch

summary(INPUT)

A = 0
B = 0

print("A:", A)
print("B:", B)
