from std import *
import copy
import re
import functools
import itertools

DAY = "10"
INPUT = "../input/input{}.txt".format(DAY)
INPUT = "../input/test.txt"

operations = []
for line in lines(INPUT):
    operations.append([x.strip() for x in line.split()])


def simulate(ops, cb):
    x = 1
    ic = 0
    i = 0
    for op in ops:
        print(i, ic, op)
        i += 1
        ic += 1
        if op[0] == 'noop':
            cb(ic, x, op)
        if op[0] == 'addx':
            cb(ic, x, op)
            ic += 1
            cb(ic+1, x, op)
            x += int(op[1])
    return x


def signal(ic, x, op):
    if (ic - 20) % 40 == 0:
        print(ic, x, op)


a = simulate(operations, signal)
print(a)

print("A:")
print("B:")
