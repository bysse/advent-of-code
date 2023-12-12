from functools import cache

from std import *

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
# INPUT = f"../input/test{DAY}.txt"

# NOTE: Too slow for B


def validate_groups(pattern: str, groups: tuple) -> bool:
    i = 0
    for group in groups:
        rl = 0
        while i < len(pattern) and pattern[i] == '.':
            i += 1

        while i < len(pattern):
            ch = pattern[i]
            if ch == '#':
                rl += 1
            if ch == '?':
                return rl <= group
            if ch == '.':
                break
            i += 1

        if rl != group:
            return False

    while i < len(pattern):
        if pattern[i] == '#':
            return False
        i += 1

    return True


def fix_next(pattern: str):
    for i, ch in enumerate(pattern):
        if ch == '?':
            a = list(pattern)
            a[i] = '#'
            b = list(pattern)
            b[i] = '.'
            return ["".join(a), "".join(b)]
    return []


@cache
def fit_group(pattern: str, groups: tuple):
    variables = pattern.count('?')
    if variables == 0:
        return 1 if validate_groups(pattern, groups) else 0

    n = 0
    for subpattern in fix_next(pattern):
        if validate_groups(subpattern, groups):
            n += fit_group(subpattern, groups)
    return n


def unfold(pattern, groups):
    p2 = pattern[:]
    for i in range(4):
        p2.append('?')
        p2 += pattern
    return p2, list(5 * groups)


A = 0
B = 0
for line in lines(INPUT):
    pattern, b = line.split()
    group = tuple(ints(b))
    n = fit_group(pattern, group)
    A += n
print("A:", A)

for line in lines(INPUT):
    pattern, b = line.split()
    pattern_5x = "?".join(5 * [pattern])
    group_5x = 5 * tuple(ints(b))

    n = fit_group(pattern_5x, group_5x)
    B += n


print("B:", B)
