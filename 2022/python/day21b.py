from std import *

DAY = "21"
INPUT = f"../input/input{DAY}.txt"
#INPUT = "../input/test2.txt"

nodes = {}
parent = {}
reverse_op = {'+': '-', '-': '+', '*': '/', '/': '*'}

for line in lines(INPUT):
    part = line.split(":")
    value = part[1].strip()
    if ' ' in value:
        operation = value.split(' ')
        nodes[part[0]] = operation
        parent[operation[0]] = part[0]
        parent[operation[2]] = part[0]
    else:
        nodes[part[0]] = int(value)


def operation(left, op, right):
    if op == '+':
        return left + right
    if op == '-':
        return left - right
    if op == '*':
        return left * right
    if op == '/':
        return left / right
    raise Exception(f"BAD OP: {op}")


def evaluate(node):
    value = nodes[node]
    if type(value) == int:
        return value

    return operation(
        evaluate(value[0]),
        value[1],
        evaluate(value[2])
    )


def reshuffle(node, branch, result):
    if node == 'root':
        return result
    value = nodes[node]
    result = reshuffle(parent[node], node, result)
    if node == 'humn' or type(value) == int:
        return result

    other_branch = value[0] if value[2] == branch else value[2]
    other_value = evaluate(other_branch)

    if value[1] == '-' and value[2] == branch:
        return operation(other_value, '-', result)
    if value[1] == '/' and value[2] == branch:
        return operation(other_value, '/', result)

    new_result = operation(result, reverse_op[value[1]], other_value)
    return new_result


# find the other root branch opoosite humn
node = 'humn'
while parent[node] != 'root':
    node = parent[node]
other = 2 if nodes['root'][0] == node else 0

result = evaluate(nodes['root'][other])
B = reshuffle('humn', None, result)
print("B:", B)

# ((4 + (2 * (x - 3))) / 4 = 150