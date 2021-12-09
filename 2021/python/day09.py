from std import *
import re
import functools
import itertools

DAY = "09"
INPUT = "../input/input{}.txt".format(DAY)
w = 100
h = 100

#INPUT = "../input/test.txt"
#w = 10
#h = 5

data = []
for line in lines(INPUT):
    data += [int(x) for x in line]

def get(x, y):
    if x < 0 or y < 0 or x >= w or y >= h:
        return 1000
    return data[x+y*w]

low = []
risk = 0
for y in range(h):
    for x in range(w):
        v = get(x, y)
        if v < get(x-1, y) and v < get(x+1, y) and v < get(x, y-1) and v < get(x, y+1):
            risk += 1 + v
            low.append( (x,y) )

print("A:", risk)


def basin(x, y):
    visited = set()
    size = 0
    explore = { (x, y, get(x, y)) }

    while len(explore):
        discovered = []
        for x, y, height in explore:
            size += 1
            for nx, ny in tdlr2D(x, y, w, h):
                nh = get(nx, ny)
                if nh < 9 and height < nh:
                    if (nx, ny) in visited:
                        continue
                    visited.add( (nx, ny) )
                    discovered.append( (nx, ny, nh) )
        explore = discovered
    return size

basins = []
for x0, y0 in low:
    basins.append(basin(x0, y0))

R = sorted(basins, reverse=True)[0:3]

print("B:", R[0]*R[1]*R[2])
