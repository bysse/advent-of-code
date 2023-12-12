import functools

from std import *

DAY = extract(os.path.basename(__file__), r"(\d+)")[0]
INPUT = f"../input/input{DAY}.txt"


# INPUT = f"../input/test{DAY}.txt"


@functools.cache
def calculate(pattern, group_count):
    if not pattern:
        return 0 if group_count else 1

    if not group_count:
        return "#" not in pattern

    if pattern[0] == ".":
        return calculate(pattern[1:], group_count)

    result = 0
    if pattern[0] == "?":
        # speculative '.'
        result += calculate(pattern[1:], group_count)

    count = group_count[0]
    if count > len(pattern):
        # bail out
        return result

    if "." not in pattern[:count] and (count == len(pattern) or pattern[count] != "#"):
        result += calculate(pattern[count + 1:], group_count[1:])

    return result


A = 0
B = 0
for line in lines(INPUT):
    pattern, b = line.split()
    group_count = tuple(ints(b))
    pattern_5x = "?".join([pattern] * 5)
    group_count_5x = 5 * group_count

    n = calculate(pattern, group_count)
    A += n
    n = calculate(pattern_5x, group_count_5x)
    B += n

print("A:", A)
print("B:", B)
