with open('../input/input10.txt', 'r') as fd:
    num = sorted(list(map(int, [line.strip() for line in fd])))

    jolt = 0
    diff = [0,0,1]
    for i in num:
        diff[i - jolt - 1] += 1
        jolt = i
    print(diff)
    print("A:", diff[0]*diff[2])

    target = num[-1]+3
    num.append(target)
    ways = {0: 1}
    for n in num:
        ways[n] = sum([ways.get(n-dx, 0) for dx in range(1,4)])
    print("B:", ways[target])
