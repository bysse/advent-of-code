from collections import defaultdict
from math import lcm

from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test{DAY}.txt"

gates = {}
for line in lines(INPUT):
    gate, outs = line.split(" -> ")
    if gate == 'broadcaster':
        gates['broadcaster'] = Map({'op': '!', 'mem': 0, 'out': [x.strip() for x in outs.split(",")]})
        continue
    gates[gate[1:]] = Map({'op': gate[0], 'mem': {}, 'out': [x.strip() for x in outs.split(",")]})

print("digraph G {")
op = {'!': '!', '%': '\\%', '&': '&'}
for k, v in gates.items():
    name = f"\"{op[v.op]}{k}\""
    out = []
    for o in v.out:
        if o in gates:
            out.append(f"\"{op[gates[o].op]}{o}\"")
        else:
            out.append(o)
    out = ", ".join(out)
    print(f"   {name} -> {out}")
print("}")

for k, v in gates.items():
    for out in v.out:
        if out in gates and gates[out].op == '&':
            gates[out].mem[k] = False


def button(gates, initial_gate, captures, iteration):
    queue = [initial_gate]

    found = set()

    while queue:
        name, pulse, sender = queue.pop(0)

        if sender in captures and pulse:
            found.add(sender)

        if name not in gates:
            continue

        gate = gates[name]
        if gate.op == '!':
            # broadcaster
            gate.mem = pulse
            for out in gate.out:
                queue.append((out, pulse, name))

        elif gate.op == '&':
            gate.mem[sender] = pulse
            output = len(gate.mem) == 0 or not all(gate.mem.values())
            for out in gate.out:
                queue.append((out, output, name))

        elif gate.op == '%':
            if not pulse:
                gate.mem = not gate.mem
                output = gate.mem
                for out in gate.out:
                    queue.append((out, output, name))
        else:
            raise Exception(f"Unknown gate {name}")

    return found


# xz -> mp = High
# ns -> qt = High
# sg -> ng = High
# pj -> qb = High

cycles = {}
for i in range(1, 100_000):
    found = button(gates, ('broadcaster', False, None), ['mp', 'qt', 'ng', 'qb'], i)
    for entry in found:
        if entry not in cycles:
            cycles[entry] = i
    if len(cycles) == 4:
        break

print("Cycles:", cycles)
print("B:", lcm(*cycles.values()))
