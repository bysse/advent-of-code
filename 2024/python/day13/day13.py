from std import *
import copy
import re
import functools
import itertools


def calc(machine, num_a, num_b):
    return machine['a'][0] * num_a + machine['b'][0] * num_b, machine['a'][1] * num_a + machine['b'][1] * num_b


def solve_a(data):
    goal = data['goal']
    a = data['a']
    b = data['b']

    num_a = 0
    num_b = int(min(goal[0] / b[0], goal[1] / b[1]))

    while num_b >= 0:
        value = calc(data, num_a, num_b)
        print(num_a, num_b, value, goal)
        if value == goal:
            print("ok")
            return num_a*2 + num_b

        while goal[0]-value[0] >= a[0] and goal[1]-value[1] >= a[1]:
            num_a += 1
        num_b-=1

    return 0


def main(input_file):
    data = []
    for group in groups(input_file):
        data.append({
            'a': ints(group[0]),
            'b': ints(group[1]),
            'goal': ints(group[2]),
        })

    A = 0
    B = 0

    for machine in data:
        A += solve_a(machine)

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    # main("input.txt")
    main("test.txt")
