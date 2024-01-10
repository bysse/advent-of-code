import heapq

from std import *

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
# INPUT = f"../input/test{DAY}.txt"

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


def explore_inf(data, start, max_steps, bounds):
    w, h = max(data)

    positions = {start}
    reached = {}

    for i in range(max_steps):
        next_pos = set()
        for pos in positions:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                np = (pos[0] + dx, pos[1] + dy)
                mnp = (np[0] % w, np[1] % h)
                if data[mnp] != '.':
                    continue
                next_pos.add(np)
                reached.setdefault(np, i + 1)
        positions = next_pos

    limited = {}
    for pos, steps in reached.items():
        if bounds[0] <= pos[0] < bounds[2] and bounds[1] <= pos[1] < bounds[3]:
            limited[pos] = steps

    return limited


A = explore(data, start, 64)

N = 26501365
G = int(N/131)

print("   617361073602319")

parity = [(N + 1) * (N + 1), N * N]
print(f"For {G} gardens, the parity is {parity[0]} {parity[1]}")

print("Full steady state gardens:")
limited = explore_inf(data, start, 131, [0, 0, 131, 131])
positions = limited.values()
full_odd = sum([1 for p in positions if p % 2 == 1])
full_even = sum([1 for p in positions if p % 2 == 0])


print(">65 steps gardens:")
c_odd_65 = sum([1 for p in positions if p % 2 == 1 and p > 65])
c_even_65 = sum([1 for p in positions if p % 2 == 0 and p > 65])
print("  Odd:", c_odd_65)
print("  Even:", c_even_65)

B = ((G + 1) * (G + 1)) * full_odd + (G * G) * full_even - (G + 1) * c_odd_65 + G * c_even_65
print(B)
