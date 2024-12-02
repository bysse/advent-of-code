from collections import defaultdict
import copy
import re
import functools
import itertools

from std.std import *


def main():
    INPUT = f"input.txt"
    #INPUT = f"test.txt"

    first = []
    second = []
    for y in lines(INPUT):
        part = extract(y, r"(\d+)\s+(\d+)")
        first.append(int(part[0]))
        second.append(int(part[1]))

    first.sort()
    second.sort()

    A = sum(map(lambda x: abs(x[0] - x[1]), zip(first, second)))
    print("A:", A)

    count = defaultdict(int)
    for n in second:
        count[n] += 1

    B = sum(map(lambda x: x * count[x], first))

    print("B:", B)



if __name__ == "__main__":
    main()