def is_valid_a(l):
    words = set()
    for w in l.strip().split(" "):
        if w in words:
            return False
        words.add(w)
    return True

def is_valid_b(l):
    words = set()
    for w in l.strip().split(" "):
        ws = "".join(sorted(w))
        if ws in words:
            return False
        words.add(ws)
    return True

with open('../input-04.txt') as fp:
    lines = [x.strip() for x in fp.readlines()]
    a_count = 0
    b_count = 0
    for l in lines:
        if is_valid_a(l):
            a_count += 1
        if is_valid_b(l):
            b_count += 1

    print('A:', a_count)
    print('B:', b_count) # 512 too high