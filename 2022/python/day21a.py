from std import *
import copy
import re
import functools
import itertools

DAY = "21"
INPUT = f"../input/input{DAY}.txt"
#INPUT = "../input/test.txt"

nodes = {}
for line in lines(INPUT):
    part = line.split(":")
    value = part[1].strip()
    if ' ' in value:
        nodes[part[0]] = tuple(value.split(' '))
    else:
        nodes[part[0]] = int(value)


def operation(left, op, right):
    print(f"({left} {op} {right})")
    if op == '+':
        return left + right
    if op == '-':
        return left - right
    if op == '*':
        return left * right
    if op == '/':
        return left / right
    raise Exception(f"BAD OP: {op}")


def evaluate(node):
    value = nodes[node]
    if type(value) == int:
        return value

    return operation(
        evaluate(value[0]),
        value[1],
        evaluate(value[2])
    )


print("B:")
