with open("day3/input3.txt", "r") as f:
    adv_input = f.readlines()


result = 0

for line in adv_input:
    line = line.strip()
    first_index = 0
    max_num_one = 0
    for i in range(first_index, len(line) - 1):
        if int(line[i]) > max_num_one:
            max_num_one = int(line[i])
            first_index = i
    max_num_two = 0
    for i in range(len(line) - 1, first_index, -1):
        if int(line[i]) > max_num_two:
            max_num_two = int(line[i])

    result += max_num_one * 10 + max_num_two


print(result)