from std import *
import copy
import re
import functools
import itertools

DAY = "01"
INPUT = f"../input/input{DAY}.txt"
#INPUT = "../input/test.txt"

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def get_num(line):
    ns = []
    for i in range(len(line)):
        ch = line[i]
        if '0' <= ch <= '9':
            ns.append(ch)
    return ns


def get_num_b(line):
    ns = []
    for i in range(len(line)):
        ch = line[i]
        if '0' <= ch <= '9':
            ns.append(ch)
        else:
            for j in range(len(digits)):
                if line[i:].startswith(digits[j]):
                    ns.append(str(j+1))
                    i += len(digits[j])
                    break
    return ns


A = 0
B = 0
for line in lines(INPUT):
    ns = get_num(line.rstrip())
    A += int(ns[0] + ns[-1])
    ns = get_num_b(line)
    B += int(ns[0] + ns[-1])

print("A:", A)
print("B:", B)
