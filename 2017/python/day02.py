import functools
import itertools

with open('../input-02.txt') as fp:
    data = [list(map(int, x.split('\t'))) for x in fp.readlines()]    

sum = functools.reduce(lambda a, x: a + max(x) - min(x), data, 0)
print("A: {}".format(sum))

sum = 0
for line in data:
    for a, b in itertools.permutations(line, 2):
        if a % b == 0:
            sum += a / b
            break
print("B: {}".format(sum))