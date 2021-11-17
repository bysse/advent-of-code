with open('../input-01.txt') as fp:
    data = [x.strip() for x in fp.readlines()]

sum = 0
for line in data:
    prev = line[-1]
    for ch in line:
        if prev == ch:
            sum += int(ch)
        prev = ch
print("A: {}".format(sum))

sum = 0
for line in data:
    size = len(line)
    half = int(size/2)
    for i in range(size):
        if line[i] == line[(i+half) % size]:
            sum += int(line[i])
print("B: {}".format(sum))