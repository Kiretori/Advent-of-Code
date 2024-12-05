with open("day5/input5.txt", "r") as f:
    adv_input = f.read()


rules, updates = adv_input.split("\n\n")

updates = updates.splitlines()
updates = [line.split(",") for line in updates]

rules = [(x, y) for line in rules.splitlines() for x, y in [line.split("|")]]

# Part 1

incorrect_lines = []
for pair in rules:
    for i, line in enumerate(updates):
        if pair[0] in line and pair[1] in line:
            if line.index(pair[0]) > line.index(pair[1]):
                if i not in incorrect_lines: incorrect_lines.append(i)
            else:
                continue

sum = 0

for i, line in enumerate(updates):
    if not i in incorrect_lines:
        sum += int(line[len(line)//2])

print(sum)  


# Part 2 

from functools import cmp_to_key

order_map = {}
for pair in rules:
    if pair[0] not in order_map:
        order_map[pair[0]] = []
    order_map[pair[0]].append(pair[1])

def custom_order(x, y):
    if x == y:
        return 0  
    elif y in order_map.get(x, []):
        return -1 
    elif x in order_map.get(y, []):
        return 1   
    return 0 

fixed_lines = []
part2_sum = 0
for i in incorrect_lines:
    sorted_line = sorted(updates[i], key=cmp_to_key(custom_order))
    part2_sum += int(sorted_line[len(sorted_line)//2])
    
print(part2_sum)