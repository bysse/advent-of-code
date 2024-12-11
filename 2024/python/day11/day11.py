import math
from collections import defaultdict

from std import *
import copy
import re
import functools
import itertools


def get_digits(n):
    return int(math.log10(n)) + 1


def evolve_state_a(state):
    next_state = []
    for stone in state:
        if stone == 0:
            next_state.append(1)
            continue

        digits = get_digits(stone)
        if (digits & 1) == 0:
            half = int(math.pow(10, digits // 2))
            next_state.append(stone // half)
            next_state.append(stone % half)
            continue

        next_state.append(stone * 2024)
    return next_state


def main(input_file):
    with open(input_file) as f:
        state = ints(f.read())

    state_b = defaultdict(int)
    for s in state:
        state_b[s] += 1

    A = 0
    for i in range(75):
        state_b = evolve_state_b(state_b)
        if i == 24:
            A = calc_length(state_b)

    print("A:", A)
    print("B:", calc_length(state_b))

def calc_length(state):
    return sum(state.values())

def evolve_state_b(state):
    next_state = defaultdict(int)
    for stone, count in state.items():
        if stone == 0:
            next_state[1] += count
            continue

        digits = get_digits(stone)
        if (digits & 1) == 0:
            half = int(math.pow(10, digits // 2))
            next_state[stone // half] += count
            next_state[stone % half] += count
            continue

        next_state[stone * 2024] += count
    return next_state

if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
