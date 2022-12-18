import copy
import itertools

from std import *

DAY = "16"
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test.txt"

data = {}
edge_map = {}
rate_map = {}

for line in lines(INPUT):
    part = line.split(" ")
    rate = ints(part[4])[0]
    tunnels = "".join(part[9:]).split(",")
    rate_map[part[1]] = rate
    edge_map[part[1]] = {t: 1 for t in tunnels}
    data[part[1]] = (rate, tunnels)

# optimize the chart to remove nodes with 0 rate
for node in data.keys():
    if node == 'AA' or rate_map[node] > 0:
        continue

    edges = list(edge_map[node].keys())
    for start in edges:
        if start not in edge_map:
            continue
        for end in edges:
            if end == start or end not in edge_map or node not in edge_map[end]:
                continue
            cost = max(edge_map[start][node], edge_map[end][node])
            edge_map[start][end] = cost + 1
            edge_map[end][start] = cost + 1

        del edge_map[start][node]
    del rate_map[node]
    del edge_map[node]


def shortest_path(node):
    not_visited = set(edge_map.keys())
    cost_map = {node: 0}
    explore = set()
    path_map = {node: []}

    while not_visited:
        cost = cost_map[node]
        for n, c in edge_map[node].items():
            if n not in not_visited:
                continue
            if n not in cost_map or cost_map[n] > cost + c:
                cost_map[n] = cost + c
                path_map[n] = copy.deepcopy(path_map[node]) + [n]
            explore.add(n)

        not_visited.remove(node)

        if not explore:
            break

        node = sorted(explore, key=lambda x: cost_map[x])[0]
        explore.remove(node)

    return cost_map, path_map


path_cost = {}
path_step = {}
for node in edge_map.keys():
    cost, path = shortest_path(node)
    path_cost[node] = cost
    path_step[node] = path


def find_next_a(node, time, score, closed, max_time=30):
    best = score
    closed.remove(node)

    for n in closed:
        # move to node and open it
        n_time = time + path_cost[node][n] + 1
        if n_time > max_time:
            continue
        n_score = score + rate_map[n] * (max_time - n_time)

        branch = find_next_a(n, n_time, n_score, copy.copy(closed), max_time)
        if branch > best:
            best = branch

    return best


nodes = set(list(edge_map.keys()))
score_a = find_next_a('AA', 0, 0, nodes)
print("A:", score_a)

node_list = list(edge_map.keys())
node_list.remove('AA')
set_a_count = int(len(node_list) / 2)
score_b = 0
for nodes in itertools.combinations(node_list, set_a_count):
    node_set_a = set(nodes)
    node_set_b = set([x for x in node_list if x not in node_set_a])
    node_set_a.add('AA')
    node_set_b.add('AA')

    score = find_next_a('AA', 0, 0, node_set_a, 26) + find_next_a('AA', 0, 0, node_set_b, 26)
    if score > score_b:
        score_b = score

print("B:", score_b)
