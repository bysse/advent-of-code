import heapq
from collections import defaultdict
from typing import List

from std import *
import copy
import re
import functools
import itertools


def match4(pattern_set, target):
    max_length = max([len(x) for x in pattern_set])
    target_length = len(target)
    queue = {0}
    while len(queue) > 0:
        index = queue.pop()
        if index >= target_length:
            return True

        for i in range(1, max_length + 1):
            if index + i > target_length:
                break
            token = target[index:index + i]
            if token in pattern_set:
                queue.add(index + i)

    return False


def count1(pattern_set, target):
    max_length = max([len(x) for x in pattern_set])
    target_length = len(target)
    queue = defaultdict(int)
    queue[0] = 1
    count = 0
    while len(queue) > 0:
        index = sorted(queue.keys())[0]
        ways = queue.pop(index)
        if index >= target_length:
            count += ways
            continue

        for i in range(1, max_length + 1):
            if index + i > target_length:
                break
            token = target[index:index + i]
            if token in pattern_set:
                queue[index+i] += ways
    return count


def main(input_file):
    grp = list(groups(input_file))
    pattern_list = [x.strip() for x in grp[0][0].split(",")]
    pattern_list.sort(key=lambda x: -len(x))
    pattern_set = set(pattern_list)

    design_list = []
    for g in grp[1]:
        design_list.append(g)

    A = 0
    B = 0

    for design in design_list:
        print(design)
        ret = match4(pattern_set, design)
        if ret:
            A += 1
        B += count1(pattern_set, design)

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
