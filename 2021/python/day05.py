from std import *
import re
import functools
import itertools

INPUT = "../input/input05.txt"
#INPUT = "../input/test.txt"

data = []
for line in lines(INPUT):
    data.append(ints(line))
    
def between(a,b):
    return range(min(a,b), max(a,b) + 1)


field = {}
for x0,y0,x1,y1 in data:
    if x0 == x1:
        for y in between(y0, y1):
            field[(x0, y)] = 1 + field.get((x0, y), 0)
    elif y0 == y1:
        for x in between(x0, x1):
            field[(x, y0)] = 1 + field.get((x, y0), 0)

count = 0
for k, v in field.items():
    if v > 1:
        count += 1
print("A:", count)

for x0,y0,x1,y1 in data:
    if x0 != x1 and y0 != y1:
        dx = -1 if x0 > x1 else 1
        dy = -1 if y0 > y1 else 1

        field[(x0, y0)] = 1 + field.get((x0, y0), 0)
        while x0 != x1 and y0 != y1:            
            x0 += dx
            y0 += dy
            field[(x0, y0)] = 1 + field.get((x0, y0), 0)

count = 0
for k, v in field.items():
    if v > 1:
        count += 1
print("B:", count)
