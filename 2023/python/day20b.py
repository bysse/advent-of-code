from collections import defaultdict

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


for k, v in gates.items():
    for out in v.out:
        if out in gates and gates[out].op == '&':
            gates[out].mem[k] = False


def button():
    queue = [('broadcaster', False, None)]

    rx_pulses = 0
    single_low = False

    while queue:
        name, pulse, sender = queue.pop(0)

        if name == 'rx':
            if rx_pulses == 0 and pulse is False:
                single_low = True
            else:
                single_low = False

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

    return single_low


# TODO: Check path to rx and check for cycles

B = 0
iter = 1
while True:
    sl = button()
    if sl:
        B = iter
        break
    iter += 1

    if iter % 1000 == 0:
        print(iter)

print("B:", B)
