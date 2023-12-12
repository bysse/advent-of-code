from std import *

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"
#INPUT = f"../input/test{DAY}.txt"

A = 0


def validate_groups(pattern: list, groups: list) -> bool:
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


def fix_next(pattern: list):
    for i, ch in enumerate(pattern):
        if ch == '?':
            a = pattern[:]
            a[i] = '#'
            b = pattern[:]
            b[i] = '.'
            return [a, b]
    return []


def fit_group(pattern: list, groups: list):
    variables = pattern.count('?')
    if variables == 0:
        # print(" -", "".join(pattern), groups)
        return 1 if validate_groups(pattern, groups) else 0

    n = 0
    for subpattern in fix_next(pattern):
        if validate_groups(subpattern, groups):
            #print(" -", "".join(subpattern), groups)
            n += fit_group(subpattern, groups)
    return n


def unfold(pattern, groups):
    p2 = pattern[:]
    for i in range(4):
        p2.append('?')
        p2 += pattern
    return p2, list(5*groups)


for line in lines(INPUT):
    a, b = line.split()
    group = ints(b)
    total_broken = sum(group)
    an = fit_group(list(a), group)
    A += an


print("A:", A)
print("B:", "<too slow for B>")
