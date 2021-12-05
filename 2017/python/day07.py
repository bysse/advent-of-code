import re
import sys

nodes = {}
children = {}
leafs = set()
with open('../input-07.txt') as fp:
#with open('../test.txt') as fp:
    pattern = re.compile("([a-z]+) \((\d+)\)")

    for line in fp.readlines():
        name, check = pattern.findall(line)[0]
        node = {'w': int(check), 'c': set()}
        if "->" in line:
            node['c'] = [x.strip() for x in line[line.index("->")+3:].split(",")]
        else:
            leafs.add(name)
        children[name] = node['c']
        nodes[name] = node


root = next(iter(leafs))

stop = False
while not stop:
    stop = True
    for k, v in nodes.items():
        if root in v['c']:
            root = k
            stop = False
            break
    
print("A:", root)

def check(name):
    node = nodes[name]
    weight = node['w']

    if not children[name]:
        return weight
        
    child_weights = []
    for child in children[name]:
        child_weights.append(check(child))        

    if len(set(child_weights)) > 1:
        for i, w in enumerate(child_weights):
            if child_weights.count(w) == 1:
                j = 0
                while child_weights[j] == w:
                    j += 1
                print("B:", nodes[children[name][i]]['w'] - w + child_weights[j])
                sys.exit()
        
    return weight + sum(child_weights)

check(root)
