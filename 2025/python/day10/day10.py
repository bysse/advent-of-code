import heapq
from collections import defaultdict

from std import *


def apply_a(state, button):
    next_state = list(state)
    for i in button:
        next_state[i] = not next_state[i]
    return tuple(next_state)

def apply_b(state, button):
    next_state = list(state)
    for i in button:
        next_state[i] += 1
    return tuple(next_state)

def apply_c(state, button, count):
    if count == 0:
        return
    for i in button:
        state[i] += count

def get_linear_combinations(limits):
    upper = max(limits)
    n = len(limits)
    suffix_sums = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_sums[i] = suffix_sums[i + 1] + limits[i]

    def backtrack(index, current_sum, path):
        if index == n:
            yield tuple(path)
            return

        min_val = max(0, upper - current_sum - suffix_sums[index + 1])
        max_val = min(limits[index], upper - current_sum)

        for val in range(min_val, max_val + 1):
            yield from backtrack(index + 1, current_sum + val, path + [val])

    yield from backtrack(0, 0, [])


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


def is_out_of_bounds(state, goal):
    for i in range(len(goal)):
        if state[i] > goal[i]:
            return True
    return False


def find_solution(goal, queue, buttons, i):
    ok_states = set()
    for q in queue:
        ok_states.add(q)
    while queue:
        cost, state = heapq.heappop(queue)

        for button in buttons:
            next_state = apply_b(state[:], button)
            if is_out_of_bounds(next_state, goal):
                continue
            if next_state == goal:
                return [(cost + 1, next_state)]
            if next_state[i] == goal[i]:
                ok_states.add((cost + 1, next_state))
                continue

            entry = cost + 1, next_state
            if entry not in queue:
                heapq.heappush(queue, entry)
    return ok_states


def search_c(goal, buttons):
    start = tuple([0] * len(goal))
    goal = tuple(goal)

    button_per_index = defaultdict(list)
    for button in buttons:
        for i in range(len(goal)):
            if i in button:
                button_per_index[i].append(button)

    button_order = list(range(len(goal)))
    button_order.sort(key=lambda x: len(button_per_index[x]), reverse=True)

    queue = [(0, start)]
    for focus in button_order:
        states = find_solution(goal, queue, button_per_index[focus], focus)
        for cost, state in states:
            if state == goal:
                return cost

        queue = list(states)
        heapq.heapify(queue)

    return -1


def find_solution_2(goal, queue, buttons, i):
    ok_states = set()
    for q in queue:
        ok_states.add(q)

    while queue:
        cost, state = heapq.heappop(queue)

        max_iter = {}
        for j, button in enumerate(buttons):
            max_iter[j] = min([goal[i] - state[i] for i in button])

        for presses in get_linear_combinations(max_iter):
            next_state = list(state[:])

            for button, count in enumerate(presses):
                apply_c(next_state, buttons[button], count)

            next_state = tuple(next_state)

            if is_out_of_bounds(next_state, goal):
                continue
            if next_state == goal:
                return [(cost + sum(presses), next_state)]

            if next_state[i] == goal[i]:
                ok_states.add((cost + sum(presses), next_state))
                continue
    return ok_states


def search_d(goal, buttons):
    start = tuple([0] * len(goal))
    goal = tuple(goal)

    button_per_index = defaultdict(list)
    for button in buttons:
        for i in range(len(goal)):
            if i in button:
                button_per_index[i].append(button)

    button_order = list(range(len(goal)))
    button_order.sort(key=lambda x: len(button_per_index[x]), reverse=True)

    queue = [(0, start)]
    for focus in button_order:
        print(" focus =", focus, ">", len(queue))
        states = find_solution_2(goal, queue, button_per_index[focus], focus)
        for cost, state in states:
            if state == goal:
                return cost

        queue = list(states)
        heapq.heapify(queue)

    return -1


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
        cost = search_c(graph[2], graph[1])
        print(" =", cost)
        B += cost

    print("B:", B)



if __name__ == "__main__":
    # main("input.txt")
    main("test.txt")
