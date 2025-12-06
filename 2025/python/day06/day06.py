from std import *
import copy
import re
import functools
import itertools


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def isblank(n):
    for c in n:
        if c != ' ':
            return False
    return True


def digit_transpose(lines):
    max_len = max(len(line) for line in lines)
    t = []
    for i in range(max_len):
        n = ''
        for line in lines:
            index = len(line) - i - 1
            if index >= 0:
                n += line[index]
        if not isblank(n):
            t.append(int(n))
    return t


def get_columns(lines):
    cols = len(ints(lines[0]))
    columns = [len(lines[0])] * cols
    for line in lines[:-1]:
        c = 0
        blank = True
        for i, x in enumerate(line):
            if x == '\n':
                break
            if x != ' ':
                if blank:
                    columns[c] = min(columns[c], i)
                    c += 1
                blank = False
            else:
                blank = True
    return columns


def get_values(columns, line):
    r = []
    line = line.replace('\n', '')
    for i in range(len(columns)):
        start = columns[i]
        end = columns[i + 1] if i + 1 < len(columns) else len(line)
        value = line[start:end]
        r.append(value)
    return r


def main(input_file):
    data = []
    for line in lines(input_file):
        data.append(re.split(r"\s+", line.strip()))

    ops = data[-1]
    data = transpose(data)

    data_b = []
    with open(input_file, 'r') as fd:
        rows = fd.readlines()
        columns = get_columns(rows)
        for row in rows[:-1]:
            data_b.append(get_values(columns, row))

    data_b = transpose(data_b)

    A = 0
    B = 0

    for i, row in enumerate(data):
        numbers_a = list(map(int, row[:-1]))
        if row[-1] == '+':
            A += sum(numbers_a)
        elif row[-1] == '*':
            A += functools.reduce(lambda x, y: x * y, numbers_a)

    for i, row in enumerate(data_b):
        numbers_b = digit_transpose(row)
        if ops[i] == '+':
            B += sum(numbers_b)
        elif ops[i] == '*':
            B += functools.reduce(lambda x, y: x * y, numbers_b)


    print("A:", A)
    print("B:", B)

    # 9590345849372 too high
    # 9581313737063


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
