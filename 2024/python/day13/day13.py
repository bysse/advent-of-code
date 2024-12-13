from std import *
import copy
import re
import functools
import itertools


def calc(machine, num_a, num_b):
    return machine['a'][0] * num_a + machine['b'][0] * num_b, machine['a'][1] * num_a + machine['b'][1] * num_b


def solve_b(data):
    ax, ay = data['a']
    bx, by = data['b']
    gx, gy = data['goal']

    a_nom = gy * bx - gx * by
    a_den = ay * bx - ax * by

    b_nom = gy * ax - gx * ay
    b_den = ax * by - ay * bx

    if a_den == 0 or b_den == 0:
        return 0

    a = a_nom / a_den
    b = b_nom / b_den

    if int(a) != a or int(b) != b:
        return 0

    return int(a * 3 + b)


def main(input_file):
    data = []
    for group in groups(input_file):
        data.append({
            'a': ints(group[0]),
            'b': ints(group[1]),
            'goal': tuple(ints(group[2])),
        })

    A = 0
    B = 0

    for machine in data:
        A += solve_b(machine)
        machine['goal'] = (10000000000000 + machine['goal'][0], 10000000000000 + machine['goal'][1])
        B += solve_b(machine)

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
