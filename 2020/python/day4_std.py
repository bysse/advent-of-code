from std import *
from year import *
import re
import itertools

pps = readChunkedPassports("../input/input4.txt")

pps = list(filter(passportValidFields, pps))
print("A:", len(pps))

pps = list(filter(passportValidValues, pps))
print("B:", len(pps))
