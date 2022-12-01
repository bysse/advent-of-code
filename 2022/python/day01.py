from std import *
import re
import functools
import itertools

DAY = "01"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

calories = []
for group in groups(INPUT, int):
    calories.append(sum(group))

print("A:", max(calories))
print("B:", sum(top(3, calories)))
