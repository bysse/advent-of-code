from std import *
import re
import copy

DAY = "08"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"


display = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
digits = [set(x) for x in display]

data = []
for line in lines(INPUT):    
    data.append([set(x) for x in re.split(r'[\| ]+', line)])

S = 0
for signal in data:   
    solved = {}

    for item in signal:
        if len(item) == 2:
            solved[1] = item
        elif len(item) == 3:
            solved[7] = item
        elif len(item) == 4:
            solved[4] = item
        elif len(item) == 7:
            solved[8] = item

    for item in signal:
        if len(item) == 6: # 0, 6, 9
            if len(solved[4] & item) == 4:
                solved[9] = item
            elif len(solved[1] & item) == 2:
                solved[0] = item
            else:
                solved[6] = item

    for item in signal:
        if len(item) == 5: # 2, 3, 5
            if len(solved[1] & item) == 2:
                solved[3] = item
            elif len(solved[9] & item) == 5:
                solved[5] = item
            else:
                solved[2] = item
    
    T = ["".join(sorted(solved[x])) for x in range(10)]
    code = ["".join(sorted(x)) for x in signal[10:]]    
    num = int("".join([str(T.index(c)) for c in code]))

    S += num

print("B:", S)