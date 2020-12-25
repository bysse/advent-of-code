from functools import reduce

with open("../input/input6.txt", "r") as fd:    
    groups = reduce(lambda a, x: (a[:-1] + [a[-1]+[x]]) if x else (a + [[]]), [x.strip() for x in fd], [[]])
    print("A:", sum([len(set(''.join(group))) for group in groups]))
    print("B:", sum([len(reduce(lambda l1, l2: set(l1).intersection(l2), group)) for group in groups]))
