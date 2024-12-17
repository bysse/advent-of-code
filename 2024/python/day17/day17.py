from sympy import denom

from std import *
import copy
import re
import functools
import itertools


def combo_literal(value, register: Map):
    if value <= 3:
        return value
    if value == 4:
        return register.A
    if value == 5:
        return register.B
    if value == 6:
        return register.C

    raise Exception("Invalid combo literal = " + str(value))


def execute(ops, register: Map):
    ip = 0
    output = []

    while 0 <= ip < len(ops) - 1:
        op = ops[ip]
        value = ops[ip + 1]
        if op == 0: # ADV
            denominator = 1 << combo_literal(value, register)
            register.A = int(register.A / denominator)
        if op == 1: # BXL
            register.B = register.B ^ value
        if op == 2: # BST
            register.B = value & 0x3
        if op == 3: # JNZ
            if register.A != 0:
                ip = value - 2
        if op == 4: # BXC
            register.B = register.B ^ register.C
        if op == 5: # OUT
            output.append(combo_literal(value, register) & 0x3)
        if op == 6: # BDV
            denominator = 1 << combo_literal(value, register)
            register.B = int(register.A / denominator)
        if op == 7: # CDV
            denominator = 1 << combo_literal(value, register)
            register.C = int(register.A / denominator)

        ip += 2

    return output


def main(input_file):
    rows = list(lines(input_file))
    print(rows)
    register = Map({
        'A': ints(rows[0])[0],
        'B': ints(rows[1])[0],
        'C': ints(rows[2])[0]
    })
    ops = ints(rows[4])

    A = 0
    B = 0

    output = execute(ops, register)
    print(",".join([str(x) for x in output]))

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    # main("input.txt")
    main("test.txt")
