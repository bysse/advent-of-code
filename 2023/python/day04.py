from std import *

DAY = "04"
INPUT = f"../input/input{DAY}.txt"
#INPUT = "../input/test.txt"

data = []
for line in lines(INPUT):
    _, card = line.split(':')
    win, ticket = card.split('|')
    data.append((set(ints(win)), set(ints(ticket))))

A = 0
matches = []
for win, ticket in data:
    n = len(win & ticket)
    p = 1 << (n - 1) if n > 0 else 0
    A += p
    matches.append(n)

for i in range(len(matches) - 1, -1, -1):
    p = matches[i]
    s = 0
    for j in range(0, p):
        idx = i + j + 1
        if idx >= len(matches):
            break
        s += matches[idx]
    matches[i] = s + 1
B = sum(matches)

print("A:", A)
print("B:", B)
