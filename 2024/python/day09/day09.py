from collections import deque

from std import *
import copy
import re
import functools
import itertools


def main(input_file):
    data = []
    with open(input_file, 'r') as fd:
        data = [int(x) for x in fd.read().strip()]

    print("A:", compact_a(data))
    print("B:", compact_b(data))


def calc_checksum(block_id, start, length):
    cs = 0
    for b in range(length ):
        cs += block_id * (start + b)
    return cs


def compact_a(disk_map):
    queue = deque()
    for i, x in enumerate(disk_map):
        if i & 1 == 0:
            queue.append((i // 2, x))
        else:
            queue.append((-1, x))

    checksum = 0
    block_count = 0
    while queue:
        block_id, size = queue.popleft()
        #print("Block ID:", block_id, "Size:", size)
        #print(" ", queue)
        if block_id >= 0:
            checksum += calc_checksum(block_id, block_count, size)
            block_count += size
            continue

        # back-fill from the end
        if not queue:
            break

        last_id, last_size = queue.pop()
        while last_id < 0:
            if not queue:
                break
            last_id, last_size = queue.pop()

        moved_blocks = min(last_size, size)
        checksum += calc_checksum(last_id, block_count, moved_blocks)
        block_count += moved_blocks

        if size == last_size:
            continue
        elif size > last_size:
            #print(" * last block is fully consumed, pushing remainder to the front")
            queue.insert(0, (-1, size - last_size))
        if last_size > size:
            #print(" * last block is partially consumed")
            queue.append((last_id, last_size - size))

    return checksum


def merge(disk):
    i = 0
    while i < len(disk) - 1:
        if disk[i][0] == disk[i + 1][0]:
            disk[i] = (disk[i][0], disk[i][1] + disk[i + 1][1])
            del disk[i + 1]
            continue
        i += 1
    return disk


def compact_b(disk_map):
    disk = []
    for i, x in enumerate(disk_map):
        if i & 1 == 0:
            disk.append((i // 2, x))
        else:
            disk.append((-1, x))

    # read block from the end
    # then traverse the free space from the start and attempt to move it

    last = len(disk) - 1
    while last >= 0:
        last_id, last_size = disk[last]
        if last_id < 0:
            last -= 1
            continue

        # we got a block, let's try to place it
        for i, (block_id, size) in enumerate(disk):
            if block_id >= 0 or size == 0 or i >= last:
                continue

            # we have a free block, let's try to move the last block to it
            if size == last_size:
                disk[i] = (last_id, last_size)
                disk[last] = (-1, last_size)
                break
            if size > last_size:
                disk[i] = (last_id, last_size)
                disk[last] = (-1, last_size)
                disk.insert(i + 1, (-1, size - last_size))
                last += 1
                break

        disk = merge(disk)

        last -= 1

    checksum = 0
    block_num = 0
    for block_id, size in disk:
        if block_id < 0:
            block_num += size
            continue
        checksum += calc_checksum(block_id, block_num, size)
        block_num += size
    return checksum

if __name__ == "__main__":
    main("input.txt")
    #main("test.txt")
