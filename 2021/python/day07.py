from std import *

DAY = "07"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

for line in lines(INPUT):
    data = ints(line)

x0 = min(data)
x1 = max(data)

best = None
for k in range(x0, x1+1):
    fuel = sum([abs(x-k) for x in data])
    if not best or fuel < best[0]:
        best = (fuel, k)        

print("A:", best[0])

def cost(n):
    return n*(1+n) // 2

best = None
for k in range(x0, x1+1):
    fuel = sum([cost(abs(x-k)) for x in data])
    if not best or fuel < best[0]:
        best = (fuel, k)       

print("B:", best[0])


