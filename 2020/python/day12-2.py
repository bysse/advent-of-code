from std import *
from year import *
import re
import functools
import itertools

actions=[]
for line in lines("../input/input12.txt"):
    actions.append( (line[0], int(line[1:])) )


wx = 10
wy = 1
x = 0
y = 0

for op, value in actions:
    if op == 'N':
        wy += value
    elif op == 'S':
        wy -= value
    elif op == 'W':
        wx -= value
    elif op == 'E':
        wx += value
    elif op == 'F':
        for i in range(value):
            x += wx
            y += wy
    elif op == 'L':
        for i in range(int(value/90)):
            wx, wy = -wy, wx
    elif op == 'R':
        for i in range(int(value/90)):
            wx, wy = wy, -wx
    
    print(op, value, ":", x,y,"->", wx, wy)

print("A:", abs(x) + abs(y))
