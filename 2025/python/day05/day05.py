from std import *


def is_fresh(intervals, thing):
    for start, end in intervals:
        if start <= thing <= end:
            return True
    return False


def overlaps(a, b):
    if a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1]:
        return True
    if b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[1]:
        return True

    return False


def union(a, b):
    return min(a[0], b[0]), max(a[1], b[1])


def merge(intervals):
    count = len(intervals)
    for i in range(count):
        for j in range(i + 1, count):
            if overlaps(intervals[i], intervals[j]):
                intervals[i] = union(intervals[i], intervals[j])
                del intervals[j]
                return intervals, True
    return intervals, False


def merge_all(intervals):
    for i in range(len(intervals)):
        intervals, changed = merge(intervals)
        if not changed:
            return intervals
    return intervals

def main(input_file):
    fresh, available = groups(input_file)
    intervals = [tuple(map(int, x.split('-'))) for x in fresh]
    ingredients = list(map(int, available))

    A = 0
    B = 0

    intervals = merge_all(intervals)

    for thing in ingredients:
        if is_fresh(intervals, thing):
            A += 1

    for start, end in intervals:
        B += end - start + 1

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
