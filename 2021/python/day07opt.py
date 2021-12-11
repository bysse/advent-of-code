from std import *
from statistics import mean, median

DAY = "07"
INPUT = "../input/input{}.txt".format(DAY)

for line in lines(INPUT):
    data = ints(line)

x0 = min(data)
x1 = max(data)

# closest to the most representative value
k = median(data)
fuel = sum([abs(x-k) for x in data])
print("A:", int(fuel))

def cost(n):
    return n*(1+n) // 2

# as cost increases the mean value is the best
k = mean(data)
fuel = sum([cost(abs(x-k)) for x in data])
print("B:", int(fuel))
