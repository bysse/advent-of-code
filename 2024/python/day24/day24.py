import os.path
from collections import deque, defaultdict

from std import *
import copy
import re
import functools
import itertools


def evaluate_gate(wires, gates, output):
    if output in wires:
        return wires[output]

    a, op, b = gates[output]
    value_a = evaluate_gate(wires, gates, a)
    value_b = evaluate_gate(wires, gates, b)

    if op == 'AND':
        wires[output] = value_a & value_b
    elif op == 'OR':
        wires[output] = value_a | value_b
    elif op == 'XOR':
        wires[output] = value_a ^ value_b
    return wires[output]


def evaluate_gates(wires, gates, outputs):
    bit_value = 0
    for i, output in enumerate(sorted(outputs)):
        bit = evaluate_gate(wires, gates, output)
        bit_value += bit << i
    return bit_value


def encode_number(prefix, value, bits_in, wires):
    for i in range(bits_in + 1):
        bit = (value >> i) & 1
        wires[f"{prefix}{i:02}"] = bit


def str_gates(wire, gates, exclude=None):
    if wire not in gates:
        return wire
    if exclude and wire in exclude:
        return f"{wire}..."
    a, op, b = gates[wire]
    a = str_gates(a, gates, exclude)
    b = str_gates(b, gates, exclude)
    if len(b) > len(a):
        return f"{wire}:({b} {op} {a})"

    return f"{wire}:({a} {op} {b})"


def build_gate_tree(outputs, gates):
    gate_tree = defaultdict(set)

    def build(node):
        if node not in gates:
            return {node}
        if node in gate_tree:
            return gate_tree[node]
        a, op, b = gates[node]
        gate_tree[node] = build(a) | build(b) | {a, b}
        return gate_tree[node]

    for output in outputs:
        build(output)

    return gate_tree


def is_input(a):
    return a[0] == 'x' or a[0] == 'y'


def execute(a, b, gates, outputs):
    inputs = {}
    encode_number("x", a, 44, inputs)
    encode_number("y", b, 44, inputs)

    return evaluate_gates(inputs, gates, outputs)


def execute_for_bit(a, b, gates, outputs, n):
    inputs = {}
    encode_number("x", a, 44, inputs)
    encode_number("y", b, 44, inputs)

    ret = evaluate_gates(inputs, gates, outputs)
    print(bin(ret >> n))
    return inputs[f"z{n + 1:02}"], inputs[f"z{n:02}"]


def test_combinations(value, bit, gates, outputs):
    print("  (0+0) = ", end='')
    ok = True
    if (r := execute_for_bit(0, 0, gates, outputs, bit)) != (0, 0):
        print("  error ->", r)
        ok = False
    print("  (1+0) = ", end='')
    if (r := execute_for_bit(value, 0, gates, outputs, bit)) != (0, 1):
        print("  error ->", r)
        ok = False
    print("  (0+1) = ", end='')
    if (r := execute_for_bit(0, value, gates, outputs, bit)) != (0, 1):
        print("  error ->", r)
        ok = False

    print("  (1+1) = ", end='')
    if (r := execute_for_bit(value, value, gates, outputs, bit)) != (1, 0):
        print("  error -> in carry", r)
        ok = False
    return ok


def find_errors(gates, outputs, gate_tree):
    valid_gates = set()
    for bit in range(45):
        node = f"z{bit:02}"
        node_2 = f"z{bit + 1:02}"
        print(f"Testing bit {bit}")
        print("  ", str_gates(node, gates, valid_gates))
        value = 1 << bit
        mask = (value << 1) - 1

        if not test_combinations(value, bit, gates, outputs):
            print(f"Error at bit {bit}")
            print("  ", str_gates(node, gates))
            for gate in sorted(gate_tree[node]):
                if is_input(gate) or gate in valid_gates:
                    continue
                print("  ", gate, " = ", " ".join(gates[gate]))

            print(f"Error at bit {bit + 1}")
            print("  ", str_gates(node_2, gates))
            for gate in sorted(gate_tree[node_2]):
                if is_input(gate) or gate in valid_gates:
                    continue
                print("  ", gate, " = ", " ".join(gates[gate]))
            print("  ", node_2, " = ", " ".join(gates[node_2]))

            print(bit - 1, ":", str_gates(f"z{bit - 1:02}", gates, valid_gates))
            print(bit, ":", str_gates(node, gates, valid_gates))
            print(bit + 1, ":", str_gates(node_2, gates, valid_gates))
            return bit, gate_tree[node_2] - valid_gates
        else:
            valid_gates |= gate_tree[node]
    return 0, set()


def switch(x, a, b):
    if x == a:
        return b
    if x == b:
        return a
    return x


def get_output(output):
    # return output
    return switch(switch(switch(switch(switch(output, "z39", "mqh"), "z28", "tfb"), "bkr", "rnq"), 'hccX', 'kqpX'), "z08", "vvr")


def main(input_file):
    inputs, rules = list(groups(input_file))
    wires = {}

    for line in inputs:
        name, value = line.split(": ")
        wires[name] = int(value)

    gates = {}
    parent_tree = defaultdict(set)
    outputs = []
    for line in rules:
        part = line.split(" ")
        output = get_output(part[-1])
        gates[output] = (part[0], part[1], part[2])
        parent_tree[part[0]].add(output)
        parent_tree[part[2]].add(output)
        if output[0] == 'z':
            outputs.append(output)

    gate_tree = build_gate_tree(outputs, gates)

    # print("A:", evaluate_gates(wires, gates, outputs))
    find_errors(gates, outputs, gate_tree)

    dig(gates, outputs, gate_tree)


    swaps = sorted(["z39", "mqh", "z28", "tfb", "bkr", "rnq", "z08", "vvr"])
    print(",".join(swaps))


def dig(gates, outputs, gate_tree):
    prune = set()
    #for i in range(20):
    #    prune.add(f"z{i:02}")
    #    outputs.remove(f"z{i:02}")
    #    prune |= gate_tree[f"z{i:02}"]

    with open("graph.dot", "w") as f:
        f.write("digraph G {\n")
        for output, (a, op, b) in gates.items():
            if output in prune:
                continue
            f.write(f"{output} [label=\"{op}\", xlabel=\"{output}\"]\n")
            f.write(f"{output} -> {a}\n")
            f.write(f"{output} -> {b}\n")

        f.write("subgraph {\n")
        f.write("rank=same;\n")
        f.write(";".join(outputs))
        f.write("}\n")
        f.write("}\n")


if __name__ == "__main__":
    main("input.txt")
    # main("test.txt")
