import heapq
from collections import defaultdict, deque

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
        if op == 0:  # ADV
            denominator = 1 << combo_literal(value, register)
            register.A = int(register.A / denominator)
        if op == 1:  # BXL
            register.B = register.B ^ value
        if op == 2:  # BST
            register.B = combo_literal(value, register) & 7
        if op == 3:  # JNZ
            if register.A != 0:
                ip = value - 2
        if op == 4:  # BXC
            register.B = register.B ^ register.C
        if op == 5:  # OUT
            output.append(combo_literal(value, register) & 7)
        if op == 6:  # BDV
            denominator = 1 << combo_literal(value, register)
            register.B = int(register.A / denominator)
        if op == 7:  # CDV
            denominator = 1 << combo_literal(value, register)
            register.C = int(register.A / denominator)

        ip += 2

    register.IP = ip
    return output


def as_bin(x):
    return [1 if x & 1 else 0, 1 if x & 2 else 0, 1 if x & 4 else 0]


def find(lookup, nums, prev=None):
    if len(nums) == 0:
        return prev
    for A in lookup[nums[-1]]:
        if prev is None or (A&7) == (prev&7):
            result = find(lookup, nums[:-1], A>>3)
            if result is not None:
                return (result<<3) + (A&3)
    return None


def execute_b(ops, register: Map):
    # 2 4		:	BST	4	:	BST A	:	B = A & 7
    # 1 5		:	BXL 5	:	BXL 5	:	B = B ^ 5
    # 7 5		:	CDV	5	:	CDV B	:	C = A / 2^B
    # 1 6		:	BXL	6	:	BXL 6	:	B = B ^ 6
    # 0 3 	    :	ADV	3	:	ADV 3	: 	A = A / 2^3
    # 4 1		:	BXC	1	:	BXC	_	:	B = B ^ C
    # 5 5		:	OUT 5	:	OUT B	:	OUT B
    # 3 0		:	JNZ 0	:			: while (A != 0)

    single = ops[:-2]
    constraints = list(reversed(ops))

    queue = [(0, constraints)]

    while queue:
        acc, const = heapq.heappop(queue)
        if len(const) == 0:
            return acc

        for i in range(8):
            A = (acc<<3) + i
            output = execute(single, Map({'A': A, 'B': 0, 'C': 0}))
            if output[0] == const[0]:
                heapq.heappush(queue, (A, const[1:]))

    return -1


def test_reg(ops, registers) -> Map:
    reg = Map(registers)
    execute(ops, reg)
    return reg


def main(input_file):
    rows = list(lines(input_file))
    register = Map({
        'A': ints(rows[0])[0],
        'B': ints(rows[1])[0],
        'C': ints(rows[2])[0]
    })
    ops = ints(rows[4])

    A = ",".join([str(x) for x in execute(ops, register)])
    B = execute_b(ops, register)

    print("Result:  ", execute(ops, Map({'A': B, 'B': 0, 'C': 0})))
    print("Expected:", ops)

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
    pass
