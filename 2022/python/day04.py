from std import *
import re
import functools
import itertools

DAY = "04"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

pairs = []
for line in lines(INPUT):
    pairs.append([tuple(map(int, x.split("-"))) for x in line.split(",")])


def contains(a, b):
    return a[0] <= b[0] and b[1] <= a[1]


def overlap(a, b):
    return a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1]


A = 0
B = 0
for first, second in pairs:
    if contains(first, second) or contains(second, first):
        A += 1
        B += 1
    elif overlap(first, second):
        B += 1

print("A:", A)
print("B:", B)
