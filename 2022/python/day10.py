from std import *
import copy
import re
import functools
import itertools

DAY = "10"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

operations = []
for line in lines(INPUT):
    operations.append([x.strip() for x in line.split()])


def simulate(ops, cb):
    x = 1
    ic = 1
    score = 0
    for op in ops:
        if op[0] == 'noop':
            score += cb(ic, x, op)
            ic += 1
        if op[0] == 'addx':
            score += cb(ic, x, op)
            ic += 1
            score += cb(ic, x, op)
            ic += 1
            x += int(op[1])
    return score


def signal(ic, x, op):
    if ic > 10 and (ic - 20) % 40 == 0:
        return ic * x
    return 0


A = simulate(operations, signal)
print("A:", A)

# ------------------------------------------
crt = []


def draw(ic, sprite_x, op):
    x = (ic-1) % 40
    if abs(sprite_x-x) <= 1:
        crt.append('#')
    else:
        crt.append('.')
    return 0

simulate(operations, draw)

print("B:")
i = 0
for y in range(6):
    for x in range(40):
        print(crt[i], end='')
        i += 1
    print()


