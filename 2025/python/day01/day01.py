import math

from std import *
import copy
import re
import functools
import itertools

def main(input_file):
    data = []
    for line in lines(input_file):
        turns = int(line[1:])
        data.append(turns  * (1 if line[0] == 'R' else -1))

    A = 0
    B = 0

    dial = 50
    for turn in data:
        dial_setting = dial
        dial += turn

        if dial < 0 or dial > 100:
            is_positive = dial >= 0
            laps = abs(math.floor(dial / 100))
            dial %= 100
            if not is_positive:
                if dial_setting == 0:
                    laps -= 1
                if dial == 0:
                    laps += 1
            B += laps
        else:
            dial %= 100
            if dial == 0:
                B += 1

        if dial == 0:
            A += 1

    print("A:", A)
    print("B:", B)


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")