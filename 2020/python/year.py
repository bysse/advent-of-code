from std import *



passportAttributes = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def passportValidFields(pp):
    if len(pp) < len(passportAttributes) or len(pp) > len(passportAttributes) + 1:
        return False
    for p in passportAttributes:
        if p not in pp:
            return False
    return True


def passportValidValues(pp):
    pp.byr = int(pp.byr)
    if pp.byr  < 1920 or pp.byr  > 2002:
        return False

    pp.iyr = int(pp.iyr)
    if pp.iyr < 2010 or pp.iyr > 2020:
        return False

    pp.eyr = int(pp.eyr)
    if pp.eyr < 2020 or pp.eyr > 2030:
        return False

    height = pp.hgt
    if not match("[1-9][0-9]+(in|cm)", height):
        return False

    h = int(height[:-2])
    u = height[-2:]    

    if u == 'cm' and (h < 150 or h > 193):
        return False
    if u == 'in' and (h < 59 or h > 76):
        return False
    pp.hgt = (h, u)

    if not match("#[0-9a-f]{6}", pp.hcl):
        return False

    if pp.ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: 
        return False

    if not match(r"[0-9]{9}", pp.pid):
        return False
    
    return True


def readChunkedPassports(filename):
    pps = []
    pp = Map()
    for line in lines(filename):
        if not line:
            pps.append(pp)
            pp = Map()
            continue 
        for p in [x.split(":") for x in line.split(" ")]:        
            pp[p[0]] = p[1]        
    if pp:        
        pps.append(pp)
    return pps
    