from std import *

DAY = "20"
INPUT = f"../input/input{DAY}.txt"
#INPUT = "../input/test.txt"

data = []
for line in lines(INPUT):
    data.append(int(line))


def calculate(source, iterations):
    length = len(source)
    mapping = list(range(length))
    for _ in range(iterations):
        for i, value in enumerate(source):
            if value == 0:
                continue
            source_index = mapping.index(i)
            target_index = (source_index + value) % (length - 1)

            moved = mapping.pop(source_index)
            mapping.insert(target_index, moved)
    return[source[i] for i in mapping]


def find_zero(a, offset):
    return a[(a.index(0) + offset) % len(a)]

A = 0
A += find_zero(calculate(data, 1), 1000)
A += find_zero(calculate(data, 1), 2000)
A += find_zero(calculate(data, 1), 3000)
print("A:", A)

data = [x * 811589153 for x in data]

B = 0
B += find_zero(calculate(data, 10), 1000)
B += find_zero(calculate(data, 10), 2000)
B += find_zero(calculate(data, 10), 3000)
print("B:", B)
