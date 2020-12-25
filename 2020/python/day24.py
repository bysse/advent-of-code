from std import *
from year import *
import re
import functools
import itertools

def decode(line):
    inst = []
    while line:
        if line[0] == 'e' or line[0] == 'w':
            inst.append(str(line[0]))
            line = line[1:]
        else:
            inst.append(line[0:2])
            line = line[2:]
    return inst    

instructions = []
for line in lines("../input/input24.txt"): 
    instructions.append(decode(line))

hexDir = [
    {
        'nw': (-1, 1),
        'ne': (0, 1),
        'e': (1, 0),
        'w': (-1, 0),
        'sw': (-1, -1),
        'se': (0, -1)
    },
    {
        'nw': (0, 1),
        'ne': (1, 1),
        'e': (1, 0),
        'w': (-1, 0),
        'sw': (0, -1),
        'se': (1, -1)
    }
]
   

field = {}
WHITE = 0
BLACK = 1

for inst in instructions:
    x = 0
    y = 0
    for op in inst:
        dp = hexDir[y&1][op]
        x += dp[0]
        y += dp[1]
    
    if (x,y) in field:
        field.pop((x,y))
    else:
        field[(x,y)] = BLACK
        
print("A:", len(field))


def iterate(state):
    xi = [0,0]
    yi = [0,0]
    for x, y in state.keys():
        xi = [min(xi[0], x), max(xi[1], x)]
        yi = [min(yi[0], y), max(yi[1], y)]
    
    field = {}
    for y in range(yi[0]-1, yi[1]+2):
        for x in range(xi[0]-1, xi[1]+2):
            adj = 0
            for p in [(x+i[0], y+i[1]) for i in hexDir[y&1].values()]:
                adj += 1 if p in state else 0
            
            if (x,y) in state:
                # black tile
                if 0 < adj and adj <= 2:
                    field[(x,y)] = BLACK
            else:
                # white tile
                if adj == 2:
                    field[(x,y)] = BLACK
    return field

for i in range(100):
    field = iterate(field)

print("B:", len(field))
        

