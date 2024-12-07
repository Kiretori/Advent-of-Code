import operator
from itertools import product
from tqdm import tqdm


with open("day7/input7.txt", "r") as f:
    adv_input = f.readlines()

valid_lines_sum = 0
operators = {operator.add, operator.mul}

for line in tqdm(adv_input): 
    total, right = line.split(":")
    total = int(total)
    right = [int(x) for x in right.split()]

    op_variation = list(product(operators, repeat=len(right)-1))

    for var in op_variation:
        result = right[0]
        for i, op in enumerate(var):
            result = op(result, right[i+1])

        if result == total:
            valid_lines_sum += total
            break

print(valid_lines_sum)

# Part 2

valid_lines_sum2 = 0
operators = {operator.concat, operator.add, operator.mul}


for line in tqdm(adv_input): 
    total, right = line.split(":")
    total = int(total)
    right = [int(x) for x in right.split()]

    op_variation = list(product(operators, repeat=len(right)-1))

    for var in op_variation:
        result = right[0]
        for i, op in enumerate(var):
            if op == operator.concat:
                result = int(op(str(result), str(right[i+1])))
            else:
                result = op(result, right[i+1])

        if result == total:
            valid_lines_sum2 += total
            break

print(valid_lines_sum2)
