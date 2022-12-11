from collections import defaultdict

from std import *
import copy
import re
import functools
import itertools

DAY = "11"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"


def get_op(ops):
    left = (lambda old: old) if ops[0] == 'old' else (lambda old: int(ops[0]))
    right = (lambda old: old) if ops[2] == 'old' else (lambda old: int(ops[2]))
    return (lambda o: left(o) + right(o)) if ops[1] == '+' else (lambda o: left(o) * right(o))


monkeys = []
for line in groups(INPUT):
    items = ints(line[1])
    ops = line[2].split(' ')

    f = get_op(ops[3:])

    monkey = {
        'items': items,
        'op': f,
        'test': ints(line[3])[0],
        'true': ints(line[4])[0],
        'false': ints(line[5])[0]
    }
    monkeys.append(monkey)


def monkey_business(rounds, monkeys):
    count = defaultdict(int)
    for round in range(rounds):
        for i, monkey in enumerate(monkeys):
            for item in monkey['items']:
                level = int(monkey['op'](item) / 3)
                if level % monkey['test'] == 0:
                    monkeys[monkey['true']]['items'].append(level)
                else:
                    monkeys[monkey['false']]['items'].append(level)
            count[i] += len(monkey['items'])
            monkey['items'] = []

    active = sorted(count.values(), reverse=True)
    return active[0] * active[1]


A = monkey_business(20, copy.deepcopy(monkeys))
print("A:", A)


def monkey_business_2(rounds, monkeys):
    count = defaultdict(int)

    denom = monkeys[0]['test']
    for m in monkeys[1:]:
        denom = int(lcd(denom, m['test']))

    for round in range(rounds):
        for i, monkey in enumerate(monkeys):
            for item in monkey['items']:
                level = monkey['op'](item) % denom
                if level % monkey['test'] == 0:
                    monkeys[monkey['true']]['items'].append(level)
                else:
                    monkeys[monkey['false']]['items'].append(level)
            count[i] += len(monkey['items'])
            monkey['items'] = []

    active = sorted(count.values(), reverse=True)
    return active[0] * active[1]


B = monkey_business_2(10000, copy.deepcopy(monkeys))
print("B:", B)
