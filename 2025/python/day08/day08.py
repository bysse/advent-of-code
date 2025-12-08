from collections import defaultdict

from std import *


def distance(p, q):
    return pow(p[0] - q[0], 2) + pow(p[1] - q[1], 2) + pow(p[2] - q[2], 2)


def get_closest_junction_boxes(nodes):
    junction_boxes = []

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            junction_boxes.append((distance(nodes[i], nodes[j]), i, j))

    junction_boxes.sort()
    return junction_boxes


def build_circuit(boxes, limit):
    circuits = defaultdict(set)
    box_map = {}
    circuit_id = 0

    for _, a, b in boxes:
        if limit <= 0:
            break
        limit -= 1

        ai = box_map[a] if a in box_map else -1
        bi = box_map[b] if b in box_map else -1

        if ai >= 0 and bi >= 0:
            if ai == bi:
                continue
            # merge the two circuits
            for remap in circuits[bi]:
                box_map[remap] = ai
            circuits[ai] |= circuits[bi]
            del circuits[bi]
        elif ai >= 0:
            circuits[ai].add(b)
            box_map[b] = ai
        elif bi >= 0:
            circuits[bi].add(a)
            box_map[a] = bi
        else:
            ai = circuit_id
            circuit_id += 1
            circuits[ai].add(a)
            circuits[ai].add(b)
            box_map[a] = ai
            box_map[b] = ai

    return circuits


def find_last_union(boxes, count):
    circuits = defaultdict(set)
    box_map = {}
    circuit_id = 0

    for _, a, b in boxes:
        ai = box_map[a] if a in box_map else -1
        bi = box_map[b] if b in box_map else -1

        if ai >= 0 and bi >= 0:
            if ai == bi:
                continue
            # merge the two circuits
            for remap in circuits[bi]:
                box_map[remap] = ai
            circuits[ai] |= circuits[bi]
            del circuits[bi]
        elif ai >= 0:
            circuits[ai].add(b)
            box_map[b] = ai
        elif bi >= 0:
            circuits[bi].add(a)
            box_map[a] = bi
        else:
            ai = circuit_id
            circuit_id += 1
            circuits[ai].add(a)
            circuits[ai].add(b)
            box_map[a] = ai
            box_map[b] = ai

        if len(circuits) == 1:
            for key in circuits.keys():
                if len(circuits[key]) == count:
                    return a, b


    return None, None

def main(input_file, limit):
    data = []
    for line in lines(input_file):
        data.append(tuple(ints(line)))

    boxes = get_closest_junction_boxes(data)
    circuits = build_circuit(boxes, limit)

    sizes = []
    for circuit in circuits:
        sizes.append(len(circuits[circuit]))
    sizes.sort(reverse=True)
    A = sizes[0] * sizes[1] * sizes[2]


    a, b = find_last_union(boxes, len(data))
    B = data[a][0] * data[b][0]

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    main("input.txt", 1000)
    #main("test.txt", 10)

# 8141888143
# 25272