import math
from collections import deque

from std import *

DAY = "19"
INPUT = f"../input/input{DAY}.txt"
#INPUT = "../input/test.txt"

blueprints = {}
for line in lines(INPUT):
    id, ore, clay, oo, oc, go, gs = ints(line)
    blueprints[id] = ((ore, 0, 0, 0), (clay, 0, 0, 0), (oo, oc, 0, 0), (go, 0, gs, 0))


def add(base, delta):
    return base[0] + delta[0], base[1] + delta[1], base[2] + delta[2], base[3] + delta[3]


def remove(base, delta):
    return base[0] - delta[0], base[1] - delta[1], base[2] - delta[2], base[3] - delta[3]


def fma(base, delta, mul):
    return base[0] + delta[0] * mul, base[1] + delta[1] * mul, base[2] + delta[2] * mul, base[3] + delta[3] * mul


def can_build_robot(inv, req):
    return req[0] <= inv[0] and req[1] <= inv[1] and req[2] <= inv[2]


def can_build_in_single_step(inv, req):
    return req[0] < inv[0] and req[1] < inv[1] and req[2] < inv[2]


def one(i):
    robs = [0, 0, 0, 0]
    robs[i] = 1
    return tuple(robs)


def bfs(bp, inventory, robots):
    q = deque()
    q.append((inventory, robots))

    result = (0, 0, 0, 0)
    visited = set()

    time = 0
    iter = 0
    prune = 0
    while q and time < 32:

        batch = len(q)
        for _ in range(batch):
            state = q.popleft()
            if state in visited:
                prune += 1
                continue
            visited.add(state)
            inventory, robots = state

            if inventory[3] <= result[3] - 2:
                prune += 1
                continue

            # build a geode
            if can_build_robot(inventory, bp[3]):
                q.append((add(remove(inventory, bp[3]), robots), add(robots, one(3))))
            else:
                for i in range(3):
                    if not can_build_robot(inventory, bp[i]):
                        continue
                    if can_build_in_single_step(robots, bp[i]):
                        continue
                    inventory2 = add(remove(inventory, bp[i]), robots)
                    q.append((inventory2, add(robots, one(i))))

                q.append((add(inventory, robots), robots))

        result = (0, 0, 0, 0)
        for inventory, _ in q:
            if inventory[3] > result[3]:
                result = inventory

        time += 1
    return result


B = 1
for id, bp in list(blueprints.items())[0:3]:
    result = bfs(bp, (0, 0, 0, 0), (1, 0, 0, 0))
    B *= result[3]

    print(f"{id}: {bp} = {result}")

print("B:", B)
