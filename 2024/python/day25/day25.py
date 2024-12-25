from std import *
import copy
import re
import functools
import itertools


def parse_lock(grp):
    heights = []
    for x in range(5):
        for y in range(7):
            if grp[y][x] == '.':
                heights.append(y - 1)
                break
    return heights


def parse_key(grp):
    heights = []
    for x in range(5):
        for y in range(7):
            if grp[6 - y][x] == '.':
                heights.append(y - 1)
                break
    return heights


def main(input_file):
    keys = []
    locks = []
    for grp in groups(input_file):
        if grp[0] == '#####':
            locks.append(parse_lock(grp))
        else:
            keys.append(parse_key(grp))
    A = 0
    for L in locks:
        for K in keys:
            if fits(L, K):
                A += 1
    print("A:", A)

def fits(L, K):
    for i in range(5):
        if L[i] + K[i] > 5:
            return False
    return True

if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
