from std import *
from year import *
import re
import sys
import functools
import itertools
import copy
import math
import random


data, w, h = load2D("day20-input.txt")
data = ["".join(x) for x in data]

monster=[
    re.compile(".#..#..#..#..#..#..."),
    re.compile("#....##....##....###"),
    re.compile("..................#.")   
]

replacement=[
    " O  O  O  O  O  O   ",
    "O    OO    OO    OOO",
    "                  O "   
]

def mirror(tile):        
    return ["".join(list(reversed(x))) for x in tile[:]]

def rotate(tile):
    r = []
    size = len(tile)
    for i in range(size):
        r.append("".join([tile[size-x-1][i] for x in range(size)]))
    return r

def look(line, monst):
    starts = []
    offset = 0
    while True:
        m = monst.search(line[offset:])
        if m:
            offset += m.start()
            starts.append(offset)
            offset += 1
            continue
        break
    return starts

def intersect(s0, s1):
    return list(set(s0) & set(s1))

def search(data, monster):
    matches=[]
    for y in range(len(data)-2):
        line = data[y]
        s0 = look(line, monster[0])
        if s0:
            s1 = look(data[y+1], monster[1])
            if s1:
                s2 = intersect(s0, s1)
                if s2:
                    s3 = look(data[y+2], monster[2])
                    for col in intersect(s2, s3):
                        #print("Found", y, col)
                        matches.append( (col,y) )
    
    if not matches:
        return None

    global replacement
    for x, y in matches:
        for dy in range(3):
            y2 = y + dy
            rep = replacement[dy]
            for dx in range(len(rep)):
                if rep[dx] == ' ':
                    continue
                x2 = x + dx
                data[y2] = data[y2][:x2]+"O"+data[y2][x2+1:]



    return count2D("#", data)

def fp(tile):
    return "".join(["".join(x) for x in tile])

datas = {}
for i in range(4):
    datas[fp(data)] = data
    data = rotate(data)
    flip = mirror(data)
    datas[fp(flip)] = flip

datas = list(datas.values())
#print("Variation count:", len(datas))

c = 0
for d in datas:
    #print("Variation:", c)
    r = search(d, monster)
    if r:
        print("B:", r)
    c += 1
