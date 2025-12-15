import functools
from collections import defaultdict
from typing import Dict, Tuple

from std import *


def find_combinations(buttons, lamp_count):
    button_count = len(buttons)
    for n in range(1, pow(2, button_count)):
        state = [False] * lamp_count
        presses = [0 if (n & pow(2, button)) == 0 else 1 for button in range(button_count)]
        for button, pressed in enumerate(presses):
            if pressed:
                for i in buttons[button]:
                    state[i] = not state[i]

        yield tuple(state), presses


def is_even(x):
    return x % 2 == 0


def is_all_even(joltage):
    for j in joltage:
        if not is_even(j):
            return False
    return True


def has_negative(joltage):
    for j in joltage:
        if j < 0:
            return True
    return False


def search_df(state_dictionary:Dict[Tuple[bool,...],Tuple[Tuple[int,...], int]], buttons, target):
    @functools.cache
    def iterate(joltage: Tuple[int,...]):
        if has_negative(joltage):
            return -1

        if sum(joltage) == 0:
            return 0

        if is_all_even(joltage):
            x = iterate(tuple([x // 2 for x in joltage]))
            if x >= 0:
                return 2 * x

        parity = tuple([not is_even(x) for x in joltage])
        if parity in state_dictionary:
            lowest = 1e10
            for press, cost in state_dictionary[parity]:
                x = iterate(tuple([x[0] - x[1] for x in zip(joltage, press)]))
                if x < 0:
                    continue
                lowest = min(lowest, x + cost)
            return -1 if lowest == 1e10 else lowest

        return -1

    return iterate(tuple(target))


# https://www.reddit.com/r/adventofcode/comments/1pk87hl/2025_day_10_part_2_bifurcate_your_way_to_victory/


def main(input_file):
    data = []
    for line in lines(input_file):
        parts = line.split(" ")
        goal = [(x == '#') for x in parts[0][1:-1]]
        buttons = [([int(y) for y in x[1:-1].split(',')]) for x in parts[1:-1]]
        joltage = ints(parts[-1][1:-1])
        data.append((goal, buttons, joltage))

    B = 0
    for graph in data:
        lamp_count = len(graph[0])
        buttons = graph[1]
        joltage = graph[2]

        state_dictionary = defaultdict(list)
        for state, presses in find_combinations(buttons, lamp_count):
            state_joltage = [0] * lamp_count
            for button, pressed in enumerate(presses):
                if pressed:
                    for i in buttons[button]:
                        state_joltage[i] += 1
            state_dictionary[tuple(state)].append((tuple(state_joltage), sum(presses)))

        p = search_df(state_dictionary, buttons, joltage)
        print(p)
        B += p

    print("169, 33, 75")

    # 10 12 11 = 33
    print("B:", B)


if __name__ == "__main__":
    main("input2.txt")
    #main("test.txt")
