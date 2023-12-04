from std import *
import copy
import re
import functools
import itertools

DAY = "04"
INPUT = f"../input/input{DAY}.txt"
# INPUT = "../input/test.txt"

A = 0
B = 0

data = []
for line in lines(INPUT):
    data.append(ints(line))

summary(INPUT)

print("A:", A)
print("B:", B)
