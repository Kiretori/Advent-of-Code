import re 
import itertools

with open("day3/input3.txt", "r") as f:
    adv_input = f.read()


# PART 1

mults = re.findall(pattern=r"mul\((\d{1,3}),(\d{1,3})\)", string=adv_input)


res = sum(itertools.starmap(lambda x, y: int(x) * int(y), mults))

# print(res)



# PART 2

do_splits = re.split(pattern=r"(?=do\(\))", string=adv_input)
# print(do_splits)

print("========================================================================================================================")

dont_splits = []
for split in do_splits:
    dont_split = re.split(pattern=r"(?=don't\(\))", string=split)
    dont_splits.append(dont_split)


#print(dont_splits)
flat_splits = list(itertools.chain.from_iterable(dont_splits))
#print(flat_splits)

mults2 = []
for split in flat_splits:
    if split.startswith("do()"):
        mults2.extend(re.findall(pattern=r"mul\((\d{1,3}),(\d{1,3})\)", string=split))
    elif split.startswith("don't()"):
        continue
    else:
        mults2.extend(re.findall(pattern=r"mul\((\d{1,3}),(\d{1,3})\)", string=split))


print(sum(itertools.starmap(lambda x, y: int(x) * int(y), mults2)))


# Part 1 no regex
def check_inside(inside):
    comma_count = 0
    if inside.startswith("(") and inside.endswith(")"):
        if inside[-2] == ")":
            return check_inside(inside[:-1])
        if not inside[1].isdigit():
            return False, None
        i = 2
        while i < len(inside) - 1:
            if inside[i] == ',' and comma_count == 0:
                comma_count += 1
                i += 1
            elif inside[i].isdigit():
                i += 1
            else:
                return False, None
        return True, len(inside)
    else:
        if len(inside) <= 5:
            return False, None
        else:
            return check_inside(inside[:len(inside) - 1])
    

def check_input(adv_input):
    i = 0
    pairs = []
    while i < len(adv_input):
        if adv_input[i] == 'm':
            if adv_input[i:i+3] == "mul":
                i = i + 3
                is_valid, length = check_inside(adv_input[i:i+9])
                if is_valid:
                    valid_str = adv_input[i+1:i+length-1]
                    nums = tuple(valid_str.split(","))
                    pairs.append(nums)
                    i = i + length
                else:
                    continue
            else:
                i += 1

        else:
            i += 1
    return pairs

pairs = check_input(adv_input)

print(sum(itertools.starmap(lambda x, y: int(x) * int(y), pairs)))


do_splits = adv_input.split("do()")
for i in range(1, len(do_splits)):
    do_splits[i] = "do()" + do_splits[i]

dont_splits = []
for split in do_splits:
    dont_split = split.split("don't()")
    for i in range(1, len(dont_split)):
        dont_split[i] = "don't()" + dont_split[i]

    dont_splits.append(dont_split)

print(do_splits)
print(dont_splits)
flat_splits = list(itertools.chain.from_iterable(dont_splits))

pairs2 = []
for split in flat_splits:
    if split.startswith("do()"):
        pairs2.extend(check_input(split))
    elif split.startswith("don't()"):
        continue
    else:
        pairs2.extend(check_input(split))

print(sum(itertools.starmap(lambda x, y: int(x) * int(y), pairs2)))
