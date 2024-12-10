import time 

with open("day9/input9.txt", "r") as f:
    adv_input = [int(x) for x in list(f.read())]


# PART 1
start = time.perf_counter()

left, right = 0, len(adv_input) - 1
output = []

remaining_blocks = adv_input[right]
empty_space = adv_input[left+1]
while left <= right:
    if left % 2 != 0:
        
        if empty_space < remaining_blocks:
            for i in range(empty_space):
                output.append(right >> 1)
            remaining_blocks -= empty_space
            left += 1
            empty_space = adv_input[left+1]

        elif empty_space > remaining_blocks:
            for i in range(remaining_blocks):
                output.append(right >> 1)
            empty_space -= remaining_blocks
            right -= 2
            remaining_blocks = adv_input[right]

        elif empty_space == remaining_blocks:
            for i in range(remaining_blocks):
                output.append(right >> 1)
            right -= 2
            left += 1
            remaining_blocks = adv_input[right]
            empty_space = adv_input[left+1]
        



    else:
        if left == right: 
            for i in range(remaining_blocks):
                output.append(left >> 1)
            break

        for i in range(adv_input[left]):
            output.append(left >> 1)

        left += 1

sum = sum(map(lambda pair: pair[0] * pair[1], enumerate(output)))

end = time.perf_counter()

print(sum)

print(f"Part 1: {(end - start)*1000:.6f} ms")

# PART 2
from collections import deque


def make_disk(raw_input):
    disk = []
    empty_locations = deque()
    at = 0
    for i, num in enumerate(raw_input):
        if i % 2 == 0:
            disk.extend([i >> 1] * num)
            at += num 
        else:
            disk.extend([None] * num)
            if num > 0: empty_locations.append((at, num, True))
            at += num
    return disk, empty_locations

start = time.perf_counter()

disk, empty_locations = make_disk(adv_input)


if len(adv_input) % 2 == 0:
    adv_input = adv_input[:len(adv_input) - 1]
disk_end = len(disk) - 1
for i in range(len(adv_input)-1, -1, -2):
    if disk[disk_end] != None:
        file_size = adv_input[disk[disk_end]*2]
    for j, space in enumerate(empty_locations):
        if space[0] < disk_end:
            if space[2] and space[1] == file_size:
                disk[space[0]:space[0]+file_size] = disk[disk_end-file_size+1:disk_end+1]
                disk[disk_end-file_size+1:disk_end+1] = [None] * file_size
                disk_end -= (file_size + adv_input[i - 1])
                empty_locations[j] = (space[0], space[1], False)
                break


            elif space[2] and space[1] >= file_size:
                disk[space[0]:space[0]+file_size] = disk[disk_end-file_size+1:disk_end+1]
                disk[disk_end-file_size+1:disk_end+1] = [None] * file_size
                empty_locations[j] = (space[0]+file_size, space[1] - file_size, True)
                to_skip = adv_input[i - 1]
                disk_end -= (file_size + adv_input[i - 1])
                break
    else:
        if len(empty_locations) > 0:
            empty_locations.pop()
        disk_end -= (file_size + adv_input[i - 1])


sum2 = 0

for i, n in enumerate(disk):
    if n != None:
        sum2 += n * i

end = time.perf_counter()

print(f"Part 2: {(end - start):.6f} seconds")

print(sum2)