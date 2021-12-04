from std import *
import re
import functools
import itertools

INPUT = "../input/input03.txt"

bc = []
nums = []
for line in lines(INPUT):
    nums.append(line)

for line in nums:
    for i in range(len(line)):
        if len(bc) <= i:
            bc.append([0,0])
        if line[i] == '0':
            bc[i][0] += 1
        else:
            bc[i][1] += 1

gamma = ""
epsilon = ""
for b in bc:
    if b[0] > b[1]:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print("A:", int(gamma,2)*int(epsilon,2))

ogen = nums[:]
i = 0
while len(ogen) > 1:
    bc = [0,0]
    for n in ogen:
        if n[i] == '0':
            bc[0] += 1
        else:
            bc[1] += 1
    ch = '0' if bc[0] > bc[1] else '1'
    ogen = [x for x in ogen if x[i] == ch]
    i += 1
    
co2 = nums[:]
i = 0
while len(co2) > 1:
    bc = [0,0]
    for n in co2:
        if n[i] == '0':
            bc[0] += 1
        else:
            bc[1] += 1
    ch = '1' if bc[0] > bc[1] else '0'
    co2 = [x for x in co2 if x[i] == ch]
    i += 1

print("B:", int(ogen[0], 2) * int(co2[0], 2))
