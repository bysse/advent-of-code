from std import *
import re
import math
import functools
import itertools

DAY = "18"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

def decode(n):
    deps = []
    nums = []
    depth = 0

    for s in n:
        if s == '[':
            depth += 1
        elif s == ']':
            depth -= 1
        elif s == ',':
            pass
        else:
            nums.append(int(s))
            deps.append(depth)
    return nums, deps

data = []
for line in lines(INPUT):
    data.append(decode(line))

def explode(nums, deps):
    for i in range(len(nums)-1):
        if deps[i] <= 4 or deps[i] != deps[i+1]:
            continue
        else:
            if i > 0:
                nums[i-1] += nums[i]
            if i+2 < len(nums):
                nums[i+2] += nums[i+1]

            nums.pop(i+1)
            deps.pop(i+1)

            nums[i] = 0
            deps[i] -= 1   
            return True
        
    return False

def split(nums, deps):
    if max(nums) < 10:
        return False

    for i in range(len(nums)): 
        if nums[i] >= 10:
            l = math.floor(nums[i] / 2)
            r = math.ceil(nums[i] / 2)
            nums[i] = l
            deps[i] += 1
            nums.insert(i+1, r)            
            deps.insert(i+1, deps[i])
            return True
    return False

def reduce(nums, deps):
    return explode(nums, deps) or split(nums, deps)

def mag(nums, deps):
    while len(nums) > 1:
        i = deps.index(max(deps))
        val = 3 * nums[i] + 2 * nums[i+1]
        nums[i] = val
        deps[i] -= 1
        nums.pop(i+1)
        deps.pop(i+1)
    return nums[0]


def show(nums, deps):
    print("N:", " ".join([str(x) for x in nums]))
    print("  ", " ".join([str(x) for x in deps]))


def add(n, m):
    d = [x+1 for x in (n[1] + m[1])]
    return n[0] + m[0], d


num = data[0]
for n in data[1:]:
    num = add(num, n)
    while reduce(*num):
        pass

print("A:", mag(*num))

max_mag = 0
for a, b in itertools.permutations(data, 2):
    n = add(a, b)
    while reduce(*n):
        pass
    max_mag = max(max_mag, mag(*n))

print("B:", max_mag)

