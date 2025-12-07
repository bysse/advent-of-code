from collections import defaultdict

from std import *
import copy
import re
import functools
import itertools


def main(input_file):
    data = []
    for line in lines(input_file):
        data.append(line)

    beams = defaultdict(int)

    A = 0
    B = 0

    for line in data:
        if (start := line.find('S')) >= 0:
            beams[start] = 1
            continue

        new_beams = defaultdict(int)
        splits = 0
        for x, ch in enumerate(line):
            if x in beams:
                if ch == '^':
                    splits += 1
                    new_beams[x - 1] += beams[x]
                    new_beams[x + 1] += beams[x]
                else:
                    new_beams[x] += beams[x]
        A += splits
        beams = new_beams

    B += sum(beams.values())

    print("A:", A)
    print("B:", B)

if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
