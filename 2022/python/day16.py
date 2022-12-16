from std import *
import copy
import re
import functools
import itertools

DAY = "16"
INPUT = "../input/input{}.txt".format(DAY)
INPUT = "../input/test.txt"

data = {}
for line in lines(INPUT):
    part = line.split(" ")
    rate = ints(part[4])[0]
    tunnels = "".join(part[9:]).split(",")
    data[part[1]] = (rate, tunnels)


def open_valve(way, rate):
    node, time, psi, valves, visited = way
    time += 1
    psi += rate * (30 - time)

    valves = copy.copy(valves)
    valves.add(node)

    return node, time, psi, valves, visited


def travel(way, tunnel):
    node, time, psi, valves, visited = way
    time += 1

    visited = copy.copy(visited)
    #visited.add(tunnel)

    return tunnel, time, psi, valves, visited


def append(list, entry):
    if entry not in list:
        list.append(entry)


def search():
    entry = 'AA'

    ways = [('AA', 0, 0, {'AA'}, {'AA'})]
    while ways:
        print(len(ways))
        explore = []
        for way in ways:
            node, time, psi, valves, visited = way
            if time >= 30 or len(valves) >= len(data):
                yield way

            rate, tunnels = data[node]
            action = False
            if rate > 0 and node not in valves:
                append(explore, open_valve(way, rate))
                action = True

            available = 0
            for t in tunnels:
                if t not in visited:
                    available += 1
            if available == 1:
                visited.add(node)

            for tunnel in tunnels:
                if tunnel in visited:
                    continue
                append(explore, travel(way, tunnel))
                action = True

            if not action:
                yield way

        ways = explore

best = 0
best_solution = None

for solution in search():
    if solution[2] > best:
        best = solution[2]
        best_solution = solution
        print("BEST", solution)
