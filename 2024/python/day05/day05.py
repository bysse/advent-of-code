from collections import defaultdict

from std import *
import copy
import re
import functools
import itertools


def main(input_file):
    rule_lines, pages_lines = groups(input_file)

    rules = defaultdict(lambda: set())
    for line in rule_lines:
        before, after = ints(line)
        rules[after].add(before)

    A = 0
    B = 0

    for line in pages_lines:
        pages = ints(line)

        if is_valid(pages, rules):
            A += pages[int(len(pages) / 2)]
        else:
            # order the pages
            pages = sort_pages(pages, rules)
            B += pages[int(len(pages) / 2)]

    print("A:", A)
    print("B:", B)


def sort_pages(pages, rules):
    def cmp(a, b):
        if a in rules and b in rules[a]:
            return -1
        if b in rules and a in rules[b]:
            return 1
        return 0
    pages.sort(key=functools.cmp_to_key(cmp))
    return pages


def is_valid(pages, rules):
    for i in range(len(pages)):
        first = pages[i]
        for j in range(i + 1, len(pages)):
            second = pages[j]
            if first in rules and second in rules[first]:
                return False
    return True


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
