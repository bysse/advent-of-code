from std import *
import copy
import re
import functools
import itertools

def main(input_file):
    data = []
    for line in lines(input_file):
        data.append(ints(line))

    data = {}
    for y, line in enumerate(lines(input_file)):
        for x, ch in enumerate(line):
            data[(x, y)] = ch

    summary(input_file)

    A = 0
    B = 0

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    main("input.txt")