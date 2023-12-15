from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
INPUT = f"../input/test{DAY}.txt"

A = 0
B = 0


def hash(ss):
    value = 0
    for s in ss:
        value += ord(s)
        value = (value * 17) & 0xff
    return value


data = []
ops = []
for line in lines(INPUT):
    data += [x.strip() for x in line.split(",")]

for op in data:
    fl = ints(op)
    ops.append((op, hash(op), '-' if'-' in op else '=', fl[0] if fl else -1))

for seq in data:
    A += hash(seq)


print(ops)

print("A:", A)
print("B:", B)
