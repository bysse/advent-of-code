from std import *
from year import *
import re
import functools
import itertools
import copy

data, w, h = load2D("../input/input17.txt")

def adjacent4D(x, y, z, w):
    for dw in range(-1, 2):
        for dz in range(-1, 2):
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if dw == 0 and dz == 0 and dx == 0 and dy == 0:
                        continue
                    yield (x+dx, y+dy, z+dz, w+dw) 

grid = {}
for y in range(h):
    line = data[y]
    for x in range(w):
        if line[x] == '#':
            grid[(x, y, 0, 0)] = '#'


def iterate(grid):
    state={}

    xi = [0,0]
    yi = [0,0]
    zi = [0,0]
    wi = [0,0]
    for x, y, z, w in grid.keys():
        xi = (min(xi[0], x), max(xi[1], x))
        yi = (min(yi[0], y), max(yi[1], y))
        zi = (min(zi[0], z), max(zi[1], z))
        wi = (min(wi[0], w), max(wi[1], w))

    for w in range(wi[0]-1, wi[1]+2):
        for z in range(zi[0]-1, zi[1]+2):
            for y in range(yi[0]-1, yi[1]+2):
                for x in range(xi[0]-1, xi[1]+2):
                    current = grid.get( (x,y,z,w), '.' )
                    active = 0
                    for ax, ay, az, aw in adjacent4D(x, y, z, w):
                        active += 1 if grid.get( (ax, ay, az, aw), '.') == '#' else 0
                    if current == '#':
                        if active == 2 or active == 3:
                            state[ (x,y,z,w) ] = '#'
                    else:                    
                        if active == 3:
                            state[ (x,y,z,w) ] = '#'
        
    return state, (xi[0]-1, xi[1]+1), (yi[0]-1, yi[1]+1), (zi[0]-1, zi[0]+1), (wi[0]-1, wi[0]+1)


for i in range(6):
    print("----------------")
    grid2, xi, yi, zi, wi = iterate(grid)
    grid = grid2

    print("X:", xi, "Y:", yi, "Z:", zi, "W:", wi)        
    print(len(grid2))
    