import heapq

from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
INPUT = f"../input/test{DAY}.txt"

data = {}
for y, line in enumerate(lines(INPUT)):
    for x, ch in enumerate(line):
        data[(x, y)] = ch


def find_nodes(data, pos):
    max_pos = max(data)
    end_pos = (max_pos[0] - 1, max_pos[1])
    queue = [(pos, 1, 0, -1)]
    visited = set()
    node_id = 0
    nodes = {}
    last_node = -1

    slopes = {'v': (0, 1), '^': (0, -1), '<': (-1, 0), '>': (1, 0)}

    while queue:
        pos, size, id, prev = queue.pop(0)
        if pos not in data or pos in visited:
            continue
        if pos == end_pos:
            last_node = id
        visited.add(pos)
        if data[pos] in slopes:
            # slope
            delta = slopes[data[pos]]
            node_id += 1
            # NOTE: the +1 is for the cost of the 'edge'
            nodes[id] = Map({'size': size+1, 'prev': prev})
            queue.append(((pos[0] + delta[0], pos[1] + delta[1]), 0, node_id, id))

        if data[pos] == '.':
            # explore
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                np = (pos[0] + dx, pos[1] + dy)
                if np in data and data[np] != '#':
                    queue.append((np, size + 1, id, prev))

    # link the next nodes
    for id, node in nodes.items():
        if node.prev < 0:
            continue
        prev = nodes[node.prev]
        if 'next' not in prev:
            prev.next = {id}
        else:
            prev.next.add(id)

    return nodes, last_node


nodes, last = find_nodes(data, (1, 0))

# TODO: fins longest path starting from nodes[0] -> nodes[last]
# TODO: longest path = shortest path with negative weights
A = 0
queue = [(0, 0)]
visited = {}
while queue:
    cost, idx = heapq.heappop(queue)

    if idx == last:
        A = -cost + nodes[idx].size
        break

    if idx in visited and cost > visited[idx]:
        continue

    visited[idx] = cost

    c = nodes[idx].size
    for n in nodes[idx].next:
        heapq.heappush(queue, (cost - c, n))

print("A:", A)
