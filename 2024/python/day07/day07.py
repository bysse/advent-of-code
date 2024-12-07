from std import *
import copy
import re
import functools
import itertools

def main(input_file):
    data = []
    for line in lines(input_file):
        data.append(ints(line))

    A = 0
    B = 0

    for calibration in data:
        if is_possible_a(calibration[0], 0, calibration[1:]):
            A += calibration[0]
        if is_possible_b(calibration[0], 0, calibration[1:]):
            B += calibration[0]

    print("A:", A)
    print("B:", B) # 11387

def is_possible_a(result, value, operands):
    if not operands:
        return result == value
    if value > result:
        return False

    if is_possible_a(result, value + operands[0], operands[1:]):
        return True

    if is_possible_a(result, value * operands[0], operands[1:]):
        return True

    return False

def is_possible_b(result, value, operands):
    if not operands:
        return result == value
    if value > result:
        return False

    if is_possible_b(result, value + operands[0], operands[1:]):
        return True

    if is_possible_b(result, value * operands[0], operands[1:]):
        return True

    if is_possible_b(result, int(str(value) + str(operands[0])), operands[1:]):
        return True

    return False


if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")