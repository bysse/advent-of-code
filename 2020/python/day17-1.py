from std import *
from year import *
import re
import functools
import itertools
import copy

data, w, h = load2D("../input/input17.txt")

def adjacent3D(x, y, z):
    for dz in range(-1, 2):
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dz == 0 and dx == 0 and dy == 0:
                    continue
                yield (x+dx, y+dy, z+dz)            

grid = {}
for y in range(h):
    line = data[y]
    for x in range(w):
        if line[x] == '#':
            grid[(x, y, 0)] = '#'


def iterate(grid):
    state={}

    xi = [0,0]
    yi = [0,0]
    zi = [0,0]
    for x, y, z in grid.keys():
        xi = (min(xi[0], x), max(xi[1], x))
        yi = (min(yi[0], y), max(yi[1], y))
        zi = (min(zi[0], z), max(zi[1], z))

    for z in range(zi[0]-1, zi[1]+2):
        for y in range(yi[0]-1, yi[1]+2):
            for x in range(xi[0]-1, xi[1]+2):
                current = grid.get( (x,y,z), '.' )
                active = 0
                for ax, ay, az in adjacent3D(x, y, z):
                    active += 1 if grid.get( (ax, ay, az), '.') == '#' else 0
                if current == '#':
                    if active == 2 or active == 3:
                        state[ (x,y,z) ] = '#'
                else:                    
                    if active == 3:
                        state[ (x,y,z) ] = '#'
        
    return state, (xi[0]-1, xi[1]+1), (yi[0]-1, yi[1]+1), (zi[0]-1, zi[0]+1)


def display(grid, xi, yi, z):
    print(" Z =", z)
    for y in range(yi[0], yi[1]+1):
        for x in range(xi[0], xi[1]+1):
            print(grid.get( (x, y, z), '.' ), end='')
        print("")


display(grid, (0, w), (0, h), 0)

for i in range(6):
    print("----------------")
    grid2, xi, yi, zi = iterate(grid)
    grid = grid2

    print("X:", xi, "Y:", yi, "Z:", zi)
    #for z in range(zi[0], zi[1]+2):
    #    display(grid2, xi, yi, z)
        
    print(len(grid2))
    