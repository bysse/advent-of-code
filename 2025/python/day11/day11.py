import heapq
from collections import defaultdict

from std import *


def find_solutions(nodes):
    explore = ['you']
    count = 0
    while explore:
        node = heapq.heappop(explore)

        if node == 'out':
            count += 1
            continue

        for child in nodes[node]:
            heapq.heappush(explore, child)
    return count


def find_solutions_b(nodes):
    memory = defaultdict(int)

    def explore(node, dac, fft):
        if node == 'out':
            return 1 if (dac and fft) else 0
        key = node, dac, fft
        if key in memory:
            return memory[key]
        total = 0
        for child in nodes[node]:
            total += explore(child, dac or node == 'dac', fft or node == 'fft')
        memory[key] = total
        return total

    return explore('svr', False, False)


def main(input_file):
    nodes = {}
    for line in lines(input_file):
        parts = [x.rstrip(':') for x in line.split(' ')]
        nodes[parts[0]] = parts[1:]

    A = find_solutions(nodes)
    print("A:", A)
    B = find_solutions_b(nodes)
    print("B:", B)


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
