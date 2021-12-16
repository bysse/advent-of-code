from math import sqrt
from std import *
from sortedcontainers import SortedSet
import re
import functools
import itertools

DAY = "15"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

field = []
for line in lines(INPUT):
    field.append( [int(x) for x in line] )

width = len(field[0])
height = len(field)

def search():
    visited = {}
    frontier = SortedSet(key=lambda x: x[2])
    frontier.add( (0,0,0) )
    visited[(0,0)] = 0

    paths = []

    while frontier:
        x,y,cost = frontier.pop(0)        

        #print("Explore", x,y)

        if x == width-1 and y == height-1:            
            paths.append(cost)
            return cost
    
        for nx, ny in tdlr2D(x, y, width, height):
            ncost = cost + field[ny][nx]

            if (nx,ny) in visited and visited[(nx, ny)] < ncost:
                continue

            visited[(nx, ny)] = ncost
            frontier.add( (nx, ny, ncost) )

print("A:", search())


for i in range(len(field)):
    L = list(field[i])
    for m in range(1, 5):
        X = [x if x <= 9 else (x-9) for x in [x+m for x in L]]
        field[i] += X

y = len(field)
for i in range(1, 5):
    for m in range(y):
        field.append([x if x <= 9 else (x-9) for x in [x+i for x in field[m]]])

width = len(field[0])
height = len(field)

print("B:", search())
