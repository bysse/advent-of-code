from std import *

INPUT = "../input/input01.txt"
data = [int(x) for x in lines(INPUT)]

def increases(data):
    count = 0
    for i in range(1, len(data)):
        if data[i-1] < data[i]:
            count += 1
    return count

print("A:", increases(data))

sw = []
for i in range(len(data)):
    sw.append(sum(data[i:i+3]))

print("B:", increases(sw))        