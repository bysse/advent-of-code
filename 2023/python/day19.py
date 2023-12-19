from collections import defaultdict

from std import *
import copy
import re
import functools
import itertools

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test{DAY}.txt"

rr, cc = groups(INPUT)

rules = {}
parts = []

for r in rr:
    label, cond = extract(r, r"([a-z]+)\{(.*)\}")
    conditions = []
    for c in cond.split(","):
        if ':' in c:
            l, op, r, lbl = extract(c, [r"[a-z]+", r"[><]", "[0-9]+", "([a-zA-Z]+)"])
            conditions.append({'expr': (l, op, int(r)), 'label': lbl})
            continue
        conditions.append({'expr': None, 'label': c})
    rules[label] = conditions

for c in cc:
    parts.append({x[0]: int(x[2:]) for x in c[1:-1].split(',')})


def run_rules(rule, part):
    for condition in rule:
        if expr := condition['expr']:
            l, op, r = expr
            if l not in part:
                continue
            if op == '>' and part[l] > r or op == '<' and part[l] < r:
                return condition['label']
        else:
            return condition['label']
    raise Exception("No condition matched")


def accepted(part):
    next_rule = "in"
    while True:
        next_rule = run_rules(rules[next_rule], part)
        if next_rule == 'R':
            return False
        if next_rule == 'A':
            return True


A = 0
B = 0

for part in parts:
    if accepted(part):
        A += sum(part.values())

print("A:", A)


def find_constraints(rule_name, constraints):
    if rule_name == 'R':
        return 0

    if rule_name == 'A':
        solutions = 1
        for property in ['x', 'm', 'a', 's']:
            i0, i1 = constraints[property]
            if i1 < i0:
                solutions = 0
            else:
                solutions *= i1 - i0 + 1
        return solutions

    solutions = 0
    for condition in rules[rule_name]:
        if expr := condition['expr']:
            l, op, r = expr
            new_const = copy.deepcopy(constraints)
            if op == '>':
                new_const[l] = (max(new_const[l][0], r + 1), new_const[l][1])
                constraints[l] = (constraints[l][0], min(constraints[l][1], r))
            else:
                new_const[l] = (new_const[l][0], min(new_const[l][1], r-1))
                constraints[l] = (max(constraints[l][0], r), constraints[l][1])

            solutions += find_constraints(condition['label'], new_const)
        else:
            solutions += find_constraints(condition['label'], copy.deepcopy(constraints))

    return solutions


B = find_constraints('in', {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)})

print("B:", B)
