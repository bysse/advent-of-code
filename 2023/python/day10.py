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

field = {}
y = 0
width = 0
height = 0
start = None
for line in lines(INPUT):
    for x, ch in enumerate(line.strip()):
        if ch == '.':
            continue
        if ch == 'S':
            start = (x, y)
            ch = '.'
        field[(x, y)] = ch
        width = max(width, x)
    y += 1
height = y

print("Field:", field)
print("Start:", start)
print("A:", A)
print("B:", B)
