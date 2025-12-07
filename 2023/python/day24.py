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
        ii = ints(line)
        data.append((tuple(ii[0:3]), tuple(ii[3:])))

    return data


def solve(m0, k0, m1, k1):
    denom = k1 - k0
    if denom == 0:
        return -1
    return (m0 - m1) / denom


def part_a(data):
    bounds = (200000000000000, 200000000000000, 400000000000000, 400000000000000)

    for i, (p0, v0) in enumerate(data):
        k0 = v0[1] / v0[0]
        for j in range(i + 1, len(data)):
            # check for intersections between the lines
            p1, v1 = data[j]
            k1 = v1[1] / v1[0]

            x = solve(p0[0], k0, p1[0], k1)
            if x < 0:
                continue
            y = p0[0] + k0 * x
            collision = (x, y)
            if bounds[0] <= collision[0] <= bounds[2] and bounds[1] <= collision[1] <= bounds[3]:
                print("OK")

    return 0


def part_b(data):
    return 0


data = parse_input(INPUT)
print("A:", part_a(data))
print("B:", part_b(data))
