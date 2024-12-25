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


def test_bit(bit_num, wires, gates, expected):
    output_gate = f"z{bit_num:02}"
    result = evaluate_gate(wires, gates, output_gate)
    if result != expected:
        print(f"Failed {output_gate} with value {result}")
        # print(str_gates(output_gate, gates))


def test_bits(a, b, mask, gates, outputs):
    inputs = {}
    encode_number("x", a, 44, inputs)
    encode_number("y", b, 44, inputs)

    result = evaluate_gates(inputs, gates, outputs)
    return (result & mask) == ((a + b) & mask)


def str_gates(wire, gates):
    if wire not in gates:
        return wire
    a, op, b = gates[wire]
    a = str_gates(a, gates)
    b = str_gates(b, gates)
    return f"({a} {op} {b})"


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
        output = part[-1]
        gates[output] = (part[0], part[1], part[2])
        parent_tree[part[0]].add(output)
        parent_tree[part[2]].add(output)
        if output[0] == 'z':
            outputs.append(output)

    gate_tree = build_gate_tree(outputs, gates)

    # print("A:", evaluate_gates(wires, gates, outputs))

    involved = set()
    for node, (a, op, b) in gates.items():
        if is_input(a) and is_input(b):
            continue
        involved.add(node)

    print("digraph G {")
    for output, (a, op, b) in gates.items():
        print(f"{output} [label=\"{op}\", xlabel=\"{output}\"]")
        print(f"{output} -> {a}")
        print(f"{output} -> {b}")
    print("}")


def alternate(mask, gates, outputs, potential, max_faulty):
    # TODO: vary all potential gates and check if the result is correct
    potential = set([x for x in potential if x[0] != 'x' and x[0] != 'y'])

    queue = deque()
    for i in potential:
        queue.append((i, potential - {i}))

    return max_faulty


def is_correct(mask, gates, outputs):
    odd = 0x5555555
    even = 0xaaaaaaa
    return test_bits(odd, odd, mask, gates, outputs) and test_bits(even, even, mask, gates, outputs)


if __name__ == "__main__":
    main("input.txt")
    # main("test.txt")
