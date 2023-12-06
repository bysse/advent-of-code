from std import *
import copy
import re
import functools
import itertools

DAY = re.sub(r"day(\d\d).py", r"\1", os.path.basename(__file__))
INPUT = f"../input/input{DAY}.txt"
# INPUT = f"../input/test{DAY}.txt"

A = 0
B = 0

data = []
for line in lines(INPUT):
    data.append(ints(line))

summary(INPUT)

print("A:", A)
print("B:", B)
