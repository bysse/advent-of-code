from std import *
import copy
import re
import functools
import itertools


def combo_literal(value, register: Map) -> int:
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
            register.B = combo_literal(value, register) & 7
        if op == 3: # JNZ
            if register.A != 0:
                ip = value - 2
        if op == 4: # BXC
            register.B = register.B ^ register.C
        if op == 5: # OUT
            output.append(combo_literal(value, register) & 7)
        if op == 6: # BDV
            denominator = 1 << combo_literal(value, register)
            register.B = int(register.A / denominator)
        if op == 7: # CDV
            denominator = 1 << combo_literal(value, register)
            register.C = int(register.A / denominator)

        ip += 2

    register.IP = ip
    return output


def test_reg(ops, registers) -> Map:
    reg = Map(registers)
    execute(ops, reg)
    return reg

def main(input_file):
    rows = list(lines(input_file))
    print(rows)
    register = Map({
        'A': ints(rows[0])[0],
        'B': ints(rows[1])[0],
        'C': ints(rows[2])[0]
    })
    ops = ints(rows[4])

    # ADV
    assert test_reg([0, 2], {'A': 20}).A == 5
    assert test_reg([0, 5], {'A': 20, 'B':1}).A == 10
    # BXL
    assert test_reg([1, 3], {'B':3}).B == 0
    assert test_reg([1, 2], {'B':3}).B == 1
    # BST
    assert test_reg([2, 2], {'B': 0}).B == 2
    assert test_reg([2, 4], {'A': 11, 'B': 0}).B == 3
    # JNZ
    assert test_reg([3, 7], {'A': 0}).IP == 2
    assert test_reg([3, 7], {'A': 1}).IP == 7
    # BXC
    assert test_reg([4, 0], {'B': 2, 'C': 3}).B == 1
    # OUT
    assert execute([5, 3], Map({}))[0] == 3
    assert execute([5, 6], Map({'C': 11}))[0] == 3

    A = ",".join([str(x) for x in execute(ops, register)])

    B = 0

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
