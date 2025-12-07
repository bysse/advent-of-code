from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
INPUT = f"../input/test{DAY}.txt"


def parse_input(input_file):
    data = []
    for line in lines(INPUT):
        data.append(ints(line))

    data = {}
    for y, line in enumerate(lines(INPUT)):
        for x, ch in enumerate(line):
            data[(x, y)] = ch
    return data


def part_a(data):
    return 0


def part_b(data):
    return 0


data = parse_input(INPUT)
print("A:", part_a(data))
print("B:", part_b(data))
