from std import *
from year import *
from copy import deepcopy
import re
import functools
import itertools

seat = []
for line in lines("../input/input11.txt"):
    seat.append([x for x in line])

h = len(seat)
w = len(seat[0])    

def trace(x,y,dx,dy,seat):    
    for tx, ty in trace2D(x, y, dx, dy, w, h):
        if seat[ty][tx] != '.':
            return (tx, ty)
    return None


def visibleSeats(x, y, seat):
    coords = []
    for dy in range(-1, 2):
        for dx in range(-1, 2): 
            if dx == 0 and dy == 0:
                continue
            if c := trace(x,y,dx,dy,seat):
                coords.append(c)
    return coords


los = []
for y in range(h):
    row = []
    for x in range(w):
        ch = seat[y][x]
        if ch == '.':
            row.append([])
        else:
            row.append(visibleSeats(x, y, seat))
    los.append(row)

def adj(x,y,d):
    s = 0
    for sx, sy in los[y][x]:
        s += 1 if d[sy][sx] == '#' else 0
    return s

def iterate(data):
    state = deepcopy(data)   
    chx = 0 
    for y in range(h):
        for x in range(w):
            ch = data[y][x]
            o = adj(x, y, data)
            if ch == 'L' and o == 0:
                chx += 1
                state[y][x] = '#'
            elif ch == '#' and o >= 5:
                chx += 1
                state[y][x] = 'L'
    return state, chx

iter = 0
colors = {
    '.': (255,255,255),
    '#': (200, 120, 120),
    'L': (120, 120, 120),
}

while True:
    display2D(seat, colors, "images/output{:04d}.png".format(iter), load=False)
    iter += 1
    state, ch = iterate(seat)
    seat = state
    if ch == 0:
        break
display2D(seat, colors, "images/output{:04d}.png".format(iter), load=False)

print("B:", count2D('#', seat))    
