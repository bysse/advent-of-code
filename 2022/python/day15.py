from std import *
import copy
import re
import functools
import itertools

DAY = "15"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

xs = []
ys = []

data = []
for line in lines(INPUT):
    entry = ints(line)
    data.append(entry)
    xs.append(entry[0])
    xs.append(entry[2])
    ys.append(entry[1])
    ys.append(entry[3])

x0 = min(xs)
x1 = max(xs)
y0 = min(ys)
y1 = max(ys)

print(f"Size: {x1 - x0} x {y1 - y0}")


def overlaps(a, b):
    if a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1]:
        return True
    return b[0] <= a[0] and a[1] <= b[1]


def extend(a, b):
    return min(a[0], b[0]), max(a[1], b[1])


def add_interval(intervals, interval):
    for i, entry in enumerate(intervals):
        if overlaps(entry, interval):
            intervals[i] = extend(entry, interval)
            return
    intervals.append(interval)


def to_intervals(y):
    intervals = []
    for (sx, sy, bx, by) in data:
        dist = abs(sx - bx) + abs(sy - by)
        spread = dist - abs(sy - y)
        if spread < 0:
            continue
        add_interval(intervals, (sx - spread, sx + spread))

    for i in range(len(intervals)):
        for j in range(i):
            if overlaps(intervals[i], intervals[j]):
                intervals[i] = extend(intervals[i], intervals[j])
                intervals[j] = (0, 0)

    if (0, 0) in intervals:
        intervals.remove((0, 0))

    return intervals


def find_spots(y):
    intervals = to_intervals(y)
    count = 0
    for x_min, x_max in intervals:
        count += x_max - x_min
    return count


def find_spots_b(y, min_x, max_x):
    intervals = to_intervals(y)
    for i in range(len(intervals)):
        interval = intervals[i]
        intervals[i] = (max(min_x, interval[0]), min(interval[1], max_x))

    intervals.sort(key=lambda x: x[0])

    x = min_x
    for low, high in intervals:
        if x + 1 < low:
            return x + 1
        if x > high:
            continue
        x = high

    return x


A = find_spots(2000000)
#A = find_spots(11)
print("A:", A)

x_max = min(x1, 4000000)

for y in range(max(0, y0), min(y1, 4000000)):
    x = find_spots_b(y, 0, x_max)
    if x < x_max:
        B = y + x*4000000

print("B:", B)
