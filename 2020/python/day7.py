rules = {}
with open('../input/input7.txt', 'r') as fd:
    for rule in [x.strip().split(' ') for x in fd]:
        parent = "-".join(rule[0:2])
        rules[parent] = []
        if rule[4] != 'no':
            for i in range(4, len(rule), 4):
                rules[parent].append([int(rule[i]), "-".join(rule[i+1:i+3])])

def search(node, target):        
    for _, bag in rules[node]:
        if bag == target or search(bag, target):
            return True        
    return False

def count(node):    
    return 1 + sum(map(lambda x: x[0] * count(x[1]), rules[node]))

target = 'shiny-gold'
print("A:", sum(map(int, [search(x, target) for x in rules.keys() if x != target])))
print("B:", count(target) - 1)
