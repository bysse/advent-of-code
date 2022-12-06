from std import *
import copy
import re
import functools
import itertools

DAY = "06"
INPUT = "../input/input{}.txt".format(DAY)
INPUT = "../input/test.txt"

with open(INPUT) as fd:
    data = fd.read()


def find(data, size):
    buf = [0] * size
    ind = [0] * size
    dup = [0] * size
    j = 0

    for i in range(len(data)):
        ch = data[i]
        buf.index(ch)
        dup[j] = 1 if ch in buf else 0
        buf[j] = ch
        j = (j + 1) % size
        if i < size or 1 in dup:
            continue
        return i

    if 1 not in dup:
        return len(data)
    return -1

print("A:",  find(data, 4))
#print("B:", find(data, 14))
