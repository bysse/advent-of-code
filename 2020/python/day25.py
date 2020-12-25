from std import *
from year import *
import re
import sys
import functools
import itertools

data = [14082811, 5249543]
#data = [17807724, 5764801]

def encrypt(subject, loop):
    value = 1
    for _ in range(loop):
        value *= subject
        value = value % 20201227
        yield value

def encryptN(subject, loop):
    value = 1
    for _ in range(loop):
        value *= subject
        value = value % 20201227
    return value


subject = 7
n = 1
for key in encrypt(subject, 100000000):
    if key == data[0]:
        print("A:", encryptN(data[1], n), subject)
        sys.exit(0)
    n += 1

