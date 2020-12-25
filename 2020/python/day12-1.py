from std import *
from year import *
import re
import functools
import itertools

actions=[]
for line in lines("../input/input12.txt"):
    actions.append( (line[0], int(line[1:])) )


x = 0
y = 0
d = 0

for op, value in actions:
    if op == 'N':
        y += value
    elif op == 'S':
        y -= value
    elif op == 'W':
        x -= value
    elif op == 'E':
        x += value
    elif op == 'F':
        if d == 0:
            x += value
        elif d == 90:
            y -= value
        elif d == 180:
            x -= value
        elif d == 270:
            y += value
        else:
            raise Exception("DIR: " + d)
    elif op == 'L':
        d -= value
    elif op == 'R':
        d += value
    else:
        raise Exception("ERROR " + str(op))

    while d < 0:
        d += 360
    while d >= 360:
        d -= 360

print("A:", abs(x) + abs(y))