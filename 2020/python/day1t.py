#!/bin/python3
with open('../input/input1.txt', 'r') as fd:
    num = set(map(int, fd))
    print("A:", next(x*(2020-x) for x in num if (2020-x) in num))
    print("B:", next(next(x*(2020-x-n)*n for x in num if (2020-x-n) in num) for n in num))

