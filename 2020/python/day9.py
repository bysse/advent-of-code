from std import *
from year import *
import re
import functools
import itertools


num = []
for line in open('../input/input9.txt', 'r'):
    n = int(line)
    num.append(n)

def validate(num, preabmle, i):
    for j in range(i-preabmle, i):
        for k in range(i-preabmle, j):
            #print("  ", num[j],"+",num[k], "=", num[j] + num[k])
            if num[j] + num[k] == num[i]:
                return True
    return False

preabmle = 25
target = 0
for i in range(preabmle, len(num)):
    if not validate(num, 25, i):
        target = num[i]
        print("A:", num[i], "at index", i)
        break


for i in range(len(num)):
    s = 0
    for j in range(i, len(num)):
        s += num[j]
        if s == target:
            break
        if s > target:
            break
    if s == target:        
        print("B:", min(num[i:j+1]) + max(num[i:j+1]))
        break        
