from collections import defaultdict

from std import *


def apply_a(state, button):
    next_state = list(state)
    for i in button:
        next_state[i] = not next_state[i]
    return tuple(next_state)


def search_a(goal, buttons):
    start = [False] * len(goal)
    state_space = defaultdict(int)
    state_space[tuple(start)] = 0
    goal = tuple(goal)

    while True:
        next_state_space = defaultdict(int)

        for state, cost in state_space.items():
            for button in buttons:
                next_state = apply_a(state[:], button)

                next_state_space[next_state] = cost + 1

        if goal in next_state_space:
            return next_state_space[goal]

        state_space = next_state_space


def expand(ones, count):
    row = [0] * count
    for x in ones:
        row[x] = 1
    return row


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def dump(matrix, result):
    print("------")
    for i, row in enumerate(matrix):
        print(row, result[i])


def find_one(matrix, column):
    for i, row in enumerate(matrix):
        if row[column] == 1:
            return i
    return -1


def swap(matrix, i, j):
    matrix[i], matrix[j] = matrix[j], matrix[i]


import pulp

def solve_equation_system(result, buttons):
    button_count = len(buttons)
    result_count = len(result)

    model = pulp.LpProblem("Par2", pulp.LpMinimize)
    presses = [pulp.LpVariable(f"${i}", lowBound=0, cat='Integer') for i in range(button_count)]
    model += pulp.lpSum(presses)
    for i in range(result_count):
        additions = [presses[x] for x in range(button_count) if i in buttons[x]]
        model += pulp.lpSum(additions) == result[i]

    if not model.solve(pulp.PULP_CBC_CMD(msg=False)):
        raise Exception("Something when wrong")

    return int(pulp.value(model.objective))


def main(input_file):
    data = []
    for line in lines(input_file):
        parts = line.split(" ")
        goal = [(x == '#') for x in parts[0][1:-1]]
        buttons = [([int(y) for y in x[1:-1].split(',')]) for x in parts[1:-1]]
        joltage = ints(parts[-1][1:-1])
        data.append((goal, buttons, joltage))

    A = 0
    B = 0

    for graph in data:
        A += search_a(graph[0], graph[1])

    print("A:", A)

    for graph in data:
        c = solve_equation_system(graph[-1], graph[1])
        print(c)
        B += c

    print("B:", B)


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
