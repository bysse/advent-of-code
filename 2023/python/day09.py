from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test{DAY}.txt"

A = 0
B = 0


def calculate(xs):
    first = []
    last = []
    while xs:
        first.append(xs[0])
        last.append(xs[-1])
        row = []
        for i in range(1, len(xs)):
            row.append(xs[i] - xs[i - 1])
        if row.count(0) == len(row):
            break
        xs = row
    return first, last


def extrapolate_forward(dxs):
    ext = dxs[:]
    for i in range(len(dxs)-2, -1, -1):
        ext[i] += ext[i+1]
    return ext


def extrapolate_backward(dxs):
    ext = dxs[:]
    for i in range(len(dxs)-2, -1, -1):
        ext[i] -= ext[i+1]
    return ext


for line in lines(INPUT):
    first, last = calculate(ints(line))
    forward = extrapolate_forward(last)
    backward = extrapolate_backward(first)
    A += forward[0]
    B += backward[0]

print("A:", A)
print("B:", B)
