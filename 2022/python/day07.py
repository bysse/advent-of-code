from collections import defaultdict

from std import *

DAY = "07"
INPUT = "../input/input{}.txt".format(DAY)
#INPUT = "../input/test.txt"

path_map = defaultdict(dict)
child_map = defaultdict(list)
cwd = "/"

# parse
for line in lines(INPUT):
    if line.startswith("$"):
        parts = line.split(" ")
        op = parts[1]
        if op == "cd":
            arg = parts[2]
            if arg == "/":
                cwd = "/"
            elif arg == "..":
                cwd, _ = cwd.rsplit("/", maxsplit=1)
                if not len(cwd):
                    cwd = "/"
            else:
                child = cwd + ("/" if cwd != '/' else "") + arg
                child_map[cwd].append(child)
                cwd = child
        if op == "ls":
            continue
        continue

    op, name = line.split(" ")
    if op == "dir":
        name = line.split(" ")[1]
        # ignore
    else:
        path_map[cwd][name] = int(op)


# process
def recursive_size(path, size_map):
    size = sum(path_map[path].values())
    for child in child_map[path]:
        size += recursive_size(child, size_map)
    size_map[path] = size
    return size


size_map = {}
recursive_size("/", size_map)


def find_max_size(path, max_size):
    size = 0
    if size_map[path] <= max_size:
        size += size_map[path]
    for child in child_map[path]:
        size += find_max_size(child, max_size)
    return size


A = find_max_size("/", 100000)
print("A:", A)

available = 70000000
target = 30000000
free = available - size_map["/"]
remove = target - free

sorted_size = [(v, k) for k, v in size_map.items()]
sorted_size.sort(key=lambda x: x[0])

B = -1
for size, path in sorted_size:
    if size >= remove:
        B = size
        break

print("B:", B)
