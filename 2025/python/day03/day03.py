from collections import defaultdict

from std import *


def search(location, index, bank, max_index, count):
    for digit in range(9, -1, -1):
        for loc in location[digit]:
            if loc <= index or loc + count > max_index:
                continue

            if count > 1:
                score = search(location, loc, bank, max_index, count - 1)
                score += digit * 10 ** (count-1)
            else:
                score = digit

            return score

    return -1


def find_max_joltage(bank, count):
    location = defaultdict(list)
    for i, x in enumerate(bank):
        location[x].append(i)

    return search(location, -1, bank, len(bank), count)


def main(input_file):
    data = []
    for line in lines(input_file):
        data.append([int(x) for x in line])

    A = 0
    B = 0

    for bank in data:
        A += find_max_joltage(bank, 2)
        B += find_max_joltage(bank, 12)

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
