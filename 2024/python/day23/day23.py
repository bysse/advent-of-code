from collections import defaultdict

from std import *


def find_loop(a, edge_map):
    result = set()
    for b in edge_map[a]:
        if b == a:
            continue
        for c in edge_map[b]:
            if c == b or c == a:
                continue
            if a in edge_map[c]:
                result.add(tuple(sorted([a, b, c])))
    return result


def find_group(start, edge_map):
    queue = [(start, edge_map[start] | {start}, set())]

    result = set()

    while queue:
        node, potential, visited = queue.pop()
        visited.add(node)

        if potential == visited:
            result.add(tuple(sorted(potential)))
            break

        explore = potential & (edge_map[node] | {node})
        if len(explore) < 3:
            continue

        for neighbour in explore:
            if neighbour in visited:
                continue
            queue.append((neighbour, explore, set(visited)))

    return result

def search_loops(edge_map):
    priority = sorted(list(edge_map.keys()), key=lambda x: len(edge_map[x]))

    best = set()
    best_length = 0

    l = len(priority)
    for i, start in enumerate(priority):
        print(i, "of", l)
        for grp in find_group(start, edge_map):
            if len(grp) > best_length:
                best_length = len(grp)
                best = grp
    return best


def main(input_file):
    data = []
    for line in lines(input_file):
        data.append(tuple(line.split("-")))

    nodes = set()
    set_map = defaultdict(set)
    connections = defaultdict(set)
    for a, b in data:
        nodes.add(a)
        nodes.add(b)
        connections[a].add(b)
        connections[b].add(a)
        set_map[a].add(a)
        set_map[a].add(b)
        set_map[b].add(a)
        set_map[b].add(b)

    groups = set()
    for a in nodes:
        result = find_loop(a, connections)
        if result:
            for trio in result:
                if trio[0][0] == 't' or trio[1][0] == 't' or trio[2][0] == 't':
                    groups.add(trio)

    A = len(groups)

    B = "n/a"
    result = search_loops(connections)
    if result:
        B = ",".join(sorted(result))

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
