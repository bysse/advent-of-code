#!/bin/python3
import reader

def validA(entry):
    cc = 0
    for ch in entry.pw:
        if ch == entry.ch:
            cc += 1
    return entry.low <= cc and cc <= entry.high

def validB(entry):
    print(entry)
    password = entry.pw
    low = entry.low - 1
    high = entry.high - 1
    F = password[low] == entry.ch
    S = password[high] == entry.ch
    return F != S


countA = 0
countB = 0

builder = reader.Builder().tokenInt("low").discard("-").tokenInt("high").discard(" ").tokenUntil("ch", ":", discardToken=True)
builder.rest("pw", str.strip)
reader = builder.create()

for entry in reader.parse("../input/input2.txt"):
    if validA(entry):
        countA += 1
    if validB(entry):
        countB += 1   

print("A:", countA) # 5:10
print("B:", countB) # 9:30

