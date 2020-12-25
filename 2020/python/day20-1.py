from std import *
from year import *
import re
import sys
import functools
import itertools
import copy
import math
import random

tiles={}

mode = 0
tileId = -1
tile = []
size = 10

for line in lines("../input/input20.txt"):
    if not line:
        mode = 0
        tiles[tileId] = tile
        if len(tile) != size or min([len(x) for x in tile]) != size:
            print("ERROR", tileId)
            sys.exit(1)

        tile = []
        tileId = -1        
        continue
    if ":" in line:
        tileId = ints(line)[0]
        mode += 1
        continue
    if mode == 1:
        tile.append(line.strip())
if tile:
    if len(tile) != size or min([len(x) for x in tile]) != size:
        print("ERROR", tileId)
        sys.exit(1)
    tiles[tileId] = tile


def mirror(tile):        
    return ["".join(list(reversed(x))) for x in tile[:]]

def rotate(tile):
    r = []
    size = len(tile)
    for i in range(size):
        r.append("".join([tile[size-x-1][i] for x in range(size)]))
    return r

def matchesH(a, b):
    return "".join([x[-1] for x in a]) == "".join([x[0] for x in b])

def matchesV(a, b):
    return a[-1] == b[0]

side = int(math.sqrt(len(tiles)))

def fp(tile):
    return "".join(["".join(x) for x in tile])

alts = {}
for key in tiles.keys():
    tile = tiles[key]
    alt={}
    for i in range(4):
        flip = mirror(tile)    
        alt[fp(tile)] = tile
        alt[fp(flip)] = flip            
        tile = rotate(tile)
    alts[key] = list(alt.values())
    
def splice(x, i):
    return x[i], x[:i] + x[i+1:]

depth = 0

def show(field):
    print(" ")
    for y in range(0, side):
        for dy in range(1, size-1):
            line = ""
            for x in range(0, side):
                t = field[x + y*side]
                if not t:
                    line += " "*8
                else:
                    line += "".join(t[dy][1:9])
            print(line)


def matchtile(field, variant, keys, idx, resp):    
    global depth
    if idx > depth:
        depth = idx

    if idx >= 0:
        if idx >= side:
            # validate up
            if not matchesV(field[idx-side], variant):
                return False

        if idx%side > 0:
            # validate left
            if not matchesH(field[idx-1], variant):
                return False

    if not keys:
        return True                

    # try all the other alteratives for the next tile
    for i in range(len(keys)):
        key, rest = splice(keys, i)
        for variant in alts[key]:
            field[idx+1] = variant            
            if matchtile(field, variant, rest, idx+1, resp):                
                resp[idx+1] = key
                return True

    field[idx] = None
    return False
    

keys = list(alts.keys())
field = [None]*(side*side)
resp = [None]*(side*side)


if matchtile(field, None, keys, -1, resp):
    print(resp[0] * resp[side-1] * resp[(side-1)*side + 0] * resp[(side-1)*side + side - 1])
    show(field)
    sys.exit(0)

print("No solution found")
