import re

with open("day2/input2.txt", "r") as f:
    adv_input = f.read()

id_ranges_str = adv_input.split(",")

# Part 1

pattern = re.compile(r"^(\d+)\1$")

result = 0

for id_range in id_ranges_str:
    n1, n2 = id_range.split("-")
    for num in range(int(n1), int(n2) + 1):
        if bool(pattern.match(str(num))):
            result += num


print(result)

# Part 2

pattern = re.compile(r"^(\d+)\1+$")

result = 0

for id_range in id_ranges_str:
    n1, n2 = id_range.split("-")
    for num in range(int(n1), int(n2) + 1):
        if bool(pattern.match(str(num))):
            result += num


print(result)