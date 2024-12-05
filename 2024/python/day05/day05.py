from collections import defaultdict

from std import *
import copy
import re
import functools
import itertools

def main(input_file):
    rule_lines, pages_lines = groups(input_file)

    rules = defaultdict(lambda: [])
    for line in rule_lines:
        r = ints(line)
        rules[r[0]].append(r[1])

    for line in pages_lines:
        pages = ints(line)

        if is_valid(pages, rules):
            print(pages)

    A = 0
    B = 0

    print("A:", A)
    print("B:", B)


def is_valid(pages, rules):
    for i in range(1, len(pages)):
        if pages[i] in rules[pages[i-1]]:
            return False
    return True



if __name__ == "__main__":
    #main("input.txt")
    main("test.txt")