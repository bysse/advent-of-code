def redistribute(bank):
    blocks = max(bank)
    i = bank.index(blocks)

    bank[i] = 0

    while blocks > 0:
        i += 1
        if i >= len(bank):
            i = 0
        bank[i] += 1
        blocks -= 1
    return bank


with open('../input-06.txt') as fp:
    data = [int(x.strip()) for x in fp.readline().split('\t')]
  
cpy = data[:]

fps = {}
count = 0

while True:
    fp = "-".join([str(x) for x in data])
    if fp in fps:
        print("A:", count)
        print("B:", count - fps[fp])
        break
    fps[fp] = count
    data = redistribute(data)    
    count += 1