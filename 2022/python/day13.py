import functools

from std import *

DAY = "13"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"


def is_list(x):
    return type(x) == list


def compare(a, b):
    if is_list(a) and is_list(b):
        for i in range(min(len(a), len(b))):
            ret = compare(a[i], b[i])
            if ret != 0:
                return ret
        if len(a) == len(b):
            return 0
        return -1 if len(a) < len(b) else 1
    if is_list(a):
        return compare(a, [b])
    if is_list(b):
        return compare([a], b)
    if a == b:
        return 0
    return -1 if a < b else 1


packets = [
    [[2]],
    [[6]]
]
A = 0
pair = 1
for line in groups(INPUT):
    packets.append(eval(line[0]))
    packets.append(eval(line[1]))
    if -1 == compare(eval(line[0]), eval(line[1])):
        A += pair
    pair += 1

print("A:", A)


packets.sort(key=functools.cmp_to_key(compare))
str_pack = [str(x) for x in packets]
B = (1 + str_pack.index("[[2]]")) * (1 + str_pack.index("[[6]]"))

print("B:", B)
