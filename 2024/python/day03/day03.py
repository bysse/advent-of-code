from std import *
import copy
import re
import functools
import itertools


def main(input_file):
    A = 0
    B = 0

    data = []
    with open(input_file) as fp:
        data = fp.read()

    i = 0
    do = True
    while i < len(data) - 6:
        ok, offset = detect_do(data, i)
        if ok:
            do = True
            i += offset
            continue
        ok, offset = detect_dont(data, i)
        if ok:
            do = False
            i += offset
            continue

        ok, offset, a, b = detect_mul(data, i)
        if ok:
            print("mul", a, b)
            i += offset
            A += a * b

            if do:
                B += a * b
        i += 1

    print("A:", A)
    print("B:", B)


def is_num(x):
    return '0' <= x <= '9'


def read_int(data, i):
    num = 0
    for j in range(3):
        if i+j >= len(data) or not is_num(data[i + j]):
            return num, j
        num = num * 10 + int(data[i + j])
    return num, 3

def detect_do(data, i):
    if data[i:i+4] == 'do()':
        return True, 4
    return False, 1

def detect_dont(data, i):
    if data[i:i+7] == 'don\'t()':
        return True, 7
    return False, 1

def detect_mul(data, i):
    offset = i
    if data[i] == 'm' and data[i + 1] == 'u' and data[i + 2] == 'l' and data[i + 3] == '(':
        i += 4
        a, inc = read_int(data, i)
        i += inc
        if i < len(data)+2 and data[i] == ',':
            b, inc = read_int(data, i+1)
            i += inc + 1
            if i < len(data) and data[i] == ')':
                return True, i - offset, a, b
    return False, 1, 0, 0


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
