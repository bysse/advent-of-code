from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
INPUT = f"../input/test{DAY}.txt"

data = []
for line in lines(INPUT):
    data.append(ints(line))

summary(INPUT)

A = 0
B = 0

print("A:", A)
print("B:", B)
