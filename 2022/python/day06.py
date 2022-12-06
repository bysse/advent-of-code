from std import *
import copy
import re
import functools
import itertools

DAY = "06"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

with open(INPUT) as fd:
    data = fd.read()


def has_dup(buffer):
    dup = [0] * 32
    for ch in buffer:
        p = ord(ch) - ord('a')
        if dup[p] != 0:
            return True
        dup[p] += 1
    return False


def find(data, size):
    buf = [0] * size
    j = 0

    for i in range(len(data)):
        ch = data[i]
        buf[j] = ch
        j = (j + 1) % size
        if i < size or has_dup(buf):
            continue
        return i + 1
    return -1


print("A:",  find(data, 4))
print("B:", find(data, 14))
