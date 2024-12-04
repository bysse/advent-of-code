from std import *
import copy
import re
import functools
import itertools

def main(input_file):
    data = []
    for line in lines(input_file):
        data.append(line)

    A = 0
    B = 0

    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == 'X':
                A += find_words(data, x, y)
            B += is_x_mas(data, x, y)

    print("A:", A)
    print("B:", B)

def collect(data, x, y, dx, dy):
    width = len(data[0])
    height = len(data)
    seq = ""
    for i in range(4):
        xp = x + dx*i
        yp = y + dy*i
        if 0 <= xp < width and 0 <= yp < height:
            seq += data[yp][xp]
    return seq

def find_words(data, x, y):
    if data[y][x] != 'X':
        return 0

    count = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        if collect(data, x, y, dx, dy) == "XMAS":
            count += 1

    return count


def is_x_mas(data, x, y):
    width = len(data[0])
    height = len(data)

    if x < 1 or y < 1 or x >= width-1 or y >= height-1 or data[y][x] != 'A':
        return 0

    if (data[y-1][x-1] == 'M' and data[y+1][x+1] == 'S' or data[y-1][x-1] == 'S' and data[y+1][x+1] == 'M') and (data[y-1][x+1] == 'M' and data[y+1][x-1] == 'S' or data[y-1][x+1] == 'S' and data[y+1][x-1] == 'M'):
        return 1
    return 0

if __name__ == "__main__":
    #main("test.txt")
    main("input.txt")