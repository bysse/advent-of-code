from std import *
from year import *
import re
import functools
import itertools

mem={}
mask = 0
add = 0
for line in lines("../input/input14.txt"):
    if line.startswith("mask"):
        m = line.split("=")[1]
        mask = int(m.replace('X', '1'), 2)
        add = int(m.replace('X', '0'), 2)
    else:
        m = match("mem\[(\d+)\] = ([0-9]+)", line).groups()
        index = int(m[0])
        value = int(m[1])
        mem[index] = (value & mask) | add

print("A:", sum(mem.values()))

def calcMasks(m):
    pos = []
    for i in range(len(m)):
        if m[i] == 'X':
            pos.append(i)

    andPart = int(m.replace('1', 'X').replace('0', '1').replace('X', '0'),2)

    masks = []
    for v in range(0, 2**len(pos)):
        binary = ("{0:0" + str(len(pos)) + "b}").format(v)
        mask = list(m)
        for j in range(len(binary)):
            mask[pos[j]] = binary[j]
            
        masks.append((andPart, int("".join(mask), 2)))
    return masks

mem={}
masks = []
for line in lines("input14.txt"):
    if line.startswith("mask"):
        m = line.split("=")[1].strip()
        masks = calcMasks(m)
    else:
        m = match("mem\[(\d+)\] = ([0-9]+)", line).groups()
        index = int(m[0])
        value = int(m[1])
        #print("mem[{0:08b}] = {1}".format(index, value))
        for (mask, add) in masks:
            addr = (index&mask) | add
            #print("{0:08b} = {1}".format(addr, value))
            mem[addr] = value

print("B:", sum(mem.values()))