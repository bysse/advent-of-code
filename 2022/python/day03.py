from std import *
import re
import functools
import itertools

DAY = "03"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

def priority(x):
    if x.islower():
        return ord(x) - ord('a') + 1
    return (ord(x)-ord('A')) + 27

A = 0
for line in lines(INPUT):
    half = int(len(line)/2)
    a = line[:half]
    b = line[half:]
    for item in a:
        if item in b:
            A += priority(item)
            break

B = 0
data = list(lines(INPUT))
for i in range(0, len(data), 3):
    for item in data[i]:
        if item in data[i+1] and item in data[i+2]:
            B += priority(item)
            break

print("A:", A)
print("B:", B)