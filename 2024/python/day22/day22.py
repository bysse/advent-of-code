from collections import defaultdict

from std import *
import copy
import re
import functools
import itertools

def pseudo_hash(n):
    n = (n ^ (n << 6)) & 0xffffff
    n = (n ^ (n >> 5)) & 0xffffff
    n = (n ^ (n << 11)) & 0xffffff
    return n

def get_nth(seed, n):
    for i in range(n):
        seed = pseudo_hash(seed)
    return seed

def get_delta(seed, n):
    deltas = []
    seed_digit = seed % 10
    for i in range(n):
        seed_2 = pseudo_hash(seed)
        seed_2_digit = seed_2 % 10
        deltas.append(seed_2_digit - seed_digit)
        seed_digit = seed_2_digit
        seed = seed_2

        if len(deltas) > 4:
            deltas.pop(0)
        if len(deltas) == 4:
            yield tuple(deltas), seed_2_digit


def main(input_file):
    data = []
    for line in lines(input_file):
        data.append(int(line))

    A = 0
    B = 0

    for seed in data:
        A += get_nth(seed, 2000)
    print("A:", A)

    # Collect all delta sequences and their corresponding price over all seeds
    deltas = defaultdict(int)
    for seed in data:
        seed_seq = {}
        for delta, points in get_delta(seed, 2000):
            if delta not in seed_seq:
                seed_seq[delta] = points

        for delta, points in seed_seq.items():
            deltas[delta] += points

    # Find the delta sequence that has the highest price
    B = max(deltas.values())

    print("B:", B)


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")