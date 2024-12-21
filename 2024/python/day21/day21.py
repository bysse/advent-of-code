from collections import deque, defaultdict
from functools import cache

from std import *
import copy
import re
import functools
import itertools

keypad_mapping = {
    '7': (0, 3), '8': (1, 3), '9': (2, 3),
    '4': (0, 2), '5': (1, 2), '6': (2, 2),
    '1': (0, 1), '2': (1, 1), '3': (2, 1),
    'X': (0, 0), '0': (1, 0), 'A': (2, 0),
}

dpad_mapping = {
    'X': (0, 0), '^': (1, 0), 'A': (2, 0),
    '<': (0, -1), 'v': (1, -1), '>': (2, -1),
}


def movement_calculator(key_map, a, b):
    x0, y0 = key_map[a]
    x1, y1 = key_map[b]
    if x0 == x1 and y0 == y1:
        return [[]]
    if x0 == x1:
        return [[(0, y1 - y0)]]
    if y0 == y1:
        return [[(x1 - x0, 0)]]

    seq = []
    if (x1, y0) != (0, 0):
        seq.append([(x1 - x0, 0), (0, y1 - y0)])
    if (x0, y1) != (0, 0):
        seq.append([(0, y1 - y0), (x1 - x0, 0)])
    return seq


def translate(directions):
    seq = []
    for dx, dy, in directions:
        if dx == 0 and dy == 0:
            raise ValueError("Invalid direction")
        if dx == 0:
            seq.append(abs(dy) * ('^' if dy > 0 else 'v'))
        else:
            seq.append(abs(dx) * ('>' if dx > 0 else '<'))
    seq.append('A')
    return seq

@cache
def find_sequences(start_key, seq, keypad):
    queue = deque([(start_key, seq, "")])
    key_mapping = keypad_mapping if keypad else dpad_mapping

    sequences = list()

    while queue:
        pos, sequence, history = queue.pop()
        if len(sequence) == 0:
            sequences.append(history)
            continue
        movements = movement_calculator(key_mapping, pos, sequence[0])
        if not movements:
            raise ValueError("Invalid movement: %s -> %s" % (pos, sequence[0]))
        for movement in movements:
            path = "".join(translate(movement))
            queue.append((sequence[0], sequence[1:], history + path))
    min_length = min([len(x) for x in sequences])
    return set([x for x in sequences if len(x) == min_length])


def single_sequence(sequence):
    new_sequence = ""
    last_key = 'A'
    for i in range(len(sequence)):
        movements = movement_calculator(dpad_mapping, last_key, sequence[i])
        last_key = sequence[i]
        new_sequence += "".join(translate(movements[0]))
    return new_sequence


def split(s):
    last = 0
    idx = s.find('A')
    while idx >= 0:
        yield s[last:idx] + 'A'
        last = idx + 1
        idx = s.find('A', last)

def split_sequence(sequence):
    new_state = defaultdict(int)
    for part in split(sequence):
        new_state[part] += 1
    return new_state


def calculate_length(state):
    return sum([len(k) * v for k, v in state.items()])


def find_dpad_seq(sequence, count):
    sequence_map = split_sequence(sequence)
    for i in range(count):
        new_state = defaultdict(int)
        for seq, multiple in sequence_map.items():
            new_seq = single_sequence(seq)
            for part, part_count in split_sequence(new_seq).items():
                new_state[part] += part_count * multiple
        sequence_map = new_state

    return calculate_length(sequence_map)

@cache
def find_dpad_seq2(sequence, depth):
    cost = 0
    for a,b in itertools.pairwise('A' + sequence):
        movement = ["".join(translate(x)) for x in movement_calculator(dpad_mapping, a, b)]
        if depth == 0:
            cost += min([len(m) for m in movement])
        else:
            nc = [find_dpad_seq2(m, depth-1) for m in movement]
            cost += min(nc)
    return cost


def main(input_file):
    data = []
    for line in lines(input_file):
        data.append(line)

    A = 0
    B = 0

    for line in data:
        num = ints(line)[0]
        min_length_a = 1e15
        min_length_b = 1e15

        for level_1 in find_sequences('A', line, True):
            for level_2 in find_sequences('A', level_1, False):
                for level_3 in find_sequences('A', level_2, False):
                    min_length_a = min(min_length_a, len(level_3))

            min_length_b = min(min_length_b, find_dpad_seq2(level_1, 24))
        A += min_length_a * num
        B += min_length_b * num

    print("A:", A)
    print("B:", B)

if __name__ == "__main__":
    main("input.txt")
    # main("test.txt")
