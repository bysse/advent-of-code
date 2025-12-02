from std import *


def is_valid_a(s):
    if len(s) & 1 == 1:
        return True
    offset = len(s) // 2
    for i in range(offset):
        if s[i] != s[offset + i]:
            return True
    return False


def find_invalids_a(start, end):
    s = 0
    for i in range(int(start), int(end) + 1):
        if not is_valid_a(str(i)):
            s += i
    return s


def is_valid_param(s, part_length, p):
    for i in range(part_length):
        for pi in range(1, p):
            if s[i] != s[pi * part_length + i]:
                return True
    return False

def is_valid_b(s):
    length = len(s)
    found_invalid = False
    for p in range(2, length + 1):
        if length % p != 0:
            continue

        part_length = length // p
        found_invalid |= not is_valid_param(s, part_length, p)

    return not found_invalid


def find_invalids_b(start, end):
    s = 0
    for i in range(int(start), int(end) + 1):
        if not is_valid_b(str(i)):
            s += i
    return s

# 1227775554
# 4174379265

def main(input_file):
    data = []
    for line in lines(input_file):
        data += [x.split('-') for x in line.split(",")]

    A = 0
    B = 0

    for start, end in data:
        A += find_invalids_a(start, end)
        B += find_invalids_b(start, end)

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
