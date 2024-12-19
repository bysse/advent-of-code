import heapq
from typing import List

from std import *
import copy
import re
import functools
import itertools

def match(pattern_list, target):
    queue = [(0, target, [])]
    while queue:
        items, seq, path = heapq.heappop(queue)
        if not seq:
            return path
        for pattern in pattern_list:
            if seq.startswith(pattern):
                remaining = seq[len(pattern):]
                heapq.heappush(queue, (items+1, remaining, path + [pattern]))
    return None

def match2(pattern_set, target):
    max_length = max([len(x) for x in pattern_set])
    target_length = len(target)
    queue = [(0, 0)]
    while queue:
        print(queue)
        items, index = heapq.heappop(queue)
        if index >= target_length:
            return True

        for i in range(1, max_length):
            if index + i >= target_length:
                break
            token = target[index:index+i]
            if token in pattern_set:
                print("  ", token)
                heapq.heappush(queue, (items+1, index+i))

    return False



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
        break
    ret = match2(pattern_set, design_list[0])
    if ret:
        A += 1

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    #main("input.txt")
    main("test.txt")