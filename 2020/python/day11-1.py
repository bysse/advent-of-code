from std import *
from year import *
from copy import deepcopy
import re
import functools
from itertools import starmap


seat, w, h = load2D("../input/input11.txt")

def iterate(data, state):
    chx = 0 
    for x, y, ch in iterate2D(data):
        state[y][x] = ch
        if ch == '.':
            continue
        occupied = sum(map(int, starmap(lambda ax, ay: data[ay][ax] == '#', adjacent2D(x, y, w, h))))
        if ch == 'L' and occupied == 0:
            chx += 1
            state[y][x] = '#'
        elif ch == '#' and occupied >= 4:
            chx += 1
            state[y][x] = 'L'
    return chx


iter = 0
colors = {
    '.': (255,255,255),
    '#': (200, 120, 120),
    'L': (120, 120, 120),
}

data = []
data.append(deepcopy(seat))
data.append(deepcopy(seat))
buffer = 0

while True:    
    ch = iterate(data[buffer], data[1-buffer])
    buffer = (buffer+1) & 1
    if ch == 0:
        break

print("A:", count2D('#', data[buffer]))
