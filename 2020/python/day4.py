from std import *
import re
import itertools

props = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def isValid(pp):
    if len(pp) < len(props) or len(pp) > len(props) + 1:
        return False
    for p in props:
        if p not in pp:
            return False
    return True

pps = []
pp = {}
for line in lines("../input/input4.txt"):
    if not line:
        pps.append(pp)
        pp = {}
        continue 
    for p in [x.split(":") for x in line.split(" ")]:        
        pp[p[0]] = p[1]        
if pp:        
    pps.append(pp)


pps = list(filter(isValid, pps))
print("A:", len(pps))

count = 0
for pp in pps:

    byr = pp['byr']
    if len(byr) != 4 or byr[0] == '0' or int(byr) < 1920 or int(byr) > 2002:
        continue

    iyr = pp['iyr']
    if len(iyr) != 4 or iyr[0] == '0' or int(iyr) < 2010 or int(iyr) > 2020:
        continue

    eyr = pp['eyr']
    if len(eyr) != 4 or eyr[0] == '0' or int(eyr) < 2020 or int(eyr) > 2030:
        continue

    height = pp['hgt']
    if not re.match("[1-9][0-9]+(in|cm)", height):
        continue

    h = int(height[:-2])
    u = height[-2:]    

    if u == 'cm' and (h < 150 or h > 193):
        continue
    if u == 'in' and (h < 59 or h > 76):
        continue

    if not re.match("#[0-9a-f]{6}", pp['hcl']):
        continue

    if pp['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: 
        continue        

    if not match(r"[0-9]{9}", pp['pid']):
        continue
    count += 1

print("B:", count)