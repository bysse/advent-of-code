import heapq
import itertools
from collections import defaultdict

from std import *


def find_combinations(graph):
    goal = tuple(graph[0])
    buttons = graph[1]
    lamp_count = len(goal)
    button_count = len(buttons)
    for n in range(pow(2, button_count)):
        state = [False] * lamp_count
        presses = [0 if (n & pow(2, button)) == 0 else 1 for button in range(button_count)]
        for button, pressed in enumerate(presses):
            if pressed:
                for i in buttons[button]:
                    state[i] = not state[i]

        state = tuple(state)
        if state == goal:
            yield presses

# https://www.reddit.com/r/adventofcode/comments/1pk87hl/2025_day_10_part_2_bifurcate_your_way_to_victory/?share_id=57WlBoAfUvz8KFuTlJdBb&utm_content=1&utm_medium=android_app&utm_name=androidcss&utm_source=share&utm_term=1
def find_joltage(presses, buttons, joltage):
    pass


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
        presses = [x for x in find_combinations(graph)]

        find_joltage(presses, graph[1], graph[2])


    print("B:", B)


if __name__ == "__main__":
    #main("input.txt")
    main("test.txt")
