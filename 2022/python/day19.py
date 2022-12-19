from std import *
import copy
import re
import functools
import itertools

DAY = "19"
INPUT = f"../input/input{DAY}.txt"
#INPUT = "../input/test.txt"

data = {}
for line in lines(INPUT):
    id, ore, clay, oo, oc, go, gc = ints(line)
    data[id] = ((ore, 0), (clay, 0), (oo, oc), (go, gc))

print(data)

print("A:")
print("B:")
