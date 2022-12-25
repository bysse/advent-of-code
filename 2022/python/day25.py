from std import *
import copy
import re
import functools
import itertools

DAY = "25"
INPUT = f"../input/input{DAY}.txt"
#INPUT = "../input/test.txt"

VAL = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
TOK = {2: '2', 1: '1', 0: '0', -1: '-', -2: '='}


def decode(line):
    p = 5 ** (len(line) - 1)
    value = 0
    for x in line:
        value += p * VAL[x]
        p //= 5
    return value


def encode(value):
    v = []
    p = 1
    offset = 0
    while p < value:
        offset += p
        p *= 5
    offset += p
    value += 2 * offset

    while p >= 1:
        v.append(TOK[(value // p) - 2])
        value %= p
        p //= 5

    while v[0] == '0':
        v = v[1:]

    return ''.join(v)


numbers = []
for line in lines(INPUT):
    value = decode(line)
    enc = encode(value)
    #print(f"{line:6} {value:6} {enc}")
    numbers.append(value)

print("A:", encode(sum(numbers)))
