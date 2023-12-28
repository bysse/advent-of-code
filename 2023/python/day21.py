import heapq

from std import *

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test{DAY}.txt"

data = {}
start = None
for y, line in enumerate(lines(INPUT)):
    for x, ch in enumerate(line):
        if ch == 'S':
            ch = '.'
            start = (x, y)
        data[(x, y)] = ch


def explore(data, start, max_steps):
    positions = {start}
    for i in range(max_steps):
        next_pos = set()
        for pos in positions:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                np = (pos[0] + dx, pos[1] + dy)
                if np not in data:
                    continue
                if data[np] != '.':
                    continue
                next_pos.add(np)
        positions = next_pos
    return len(positions)


def explore_inf(data, start, max_steps):
    w, h = max(data)

    lpc = 1

    positions = {start}
    for i in range(max_steps):
        next_pos = set()
        for pos in positions:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                np = (pos[0] + dx, pos[1] + dy)
                mnp = (np[0] % w, np[1] % h)
                if data[mnp] != '.':
                    continue
                next_pos.add(np)
        positions = next_pos
        pc = len(positions)

        # TODO: print lit positions in original square
        print(i, pc, pc - lpc)
        lpc = pc
    return len(positions)


def dump(data, positions):
    for y in range(0, 131):
        for x in range(0, 131):
            if (x, y) in positions:
                print("#", end="")
            else:
                print(data[(x, y)], end="")
        print()

# filled maps will oscillate? only track the borders?


A = explore(data, start, 64)
B = explore_inf(data, start, 26501365)

print("A:", A)
print("B:", B)
