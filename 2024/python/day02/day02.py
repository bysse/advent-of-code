from std import *
import copy
import re
import functools
import itertools


def sign(x):
    return 1 if x > 0 else -1

def is_safe(levels):
    dir = sign(levels[0]-levels[1])
    p = levels[0]

    for i in range(1, len(levels)):
        c = levels[i]
        if abs(p-c) < 1 or abs(p-c) > 3:
            return False
        if dir != sign(p-c):
            return False
        p = c
    return True

def is_safe_b(levels):
    for i in range(0, len(levels)):
        nl = levels[0:i] + levels[i+1:]
        if is_safe(nl):
            return True
    return False


def main(input_file):
    A = 0
    B = 0

    data = []
    for line in lines(input_file):
        levels = ints(line)

        if is_safe(levels):
            A += 1
            B += 1
        else:
            if is_safe_b(levels):
                B += 1

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    main("input.txt")