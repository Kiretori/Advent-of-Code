with open("day1/input1.txt", "r") as f:
    adv_input = f.readlines()

list1 = []
list2 = []
for line in adv_input:
    pair = line.split("   ")
    list1.append(int(pair[0]))
    list2.append(int(pair[1]))


sorted_l1 = sorted(list1)
sorted_l2 = sorted(list2)

total_dist = 0

for i in range(len(sorted_l1)):
    total_dist += abs(sorted_l1[i] - sorted_l2[i])

print(total_dist)


similiraty = 0

for i in range(len(sorted_l1)):
    similiraty += sorted_l1[i] * sorted_l2.count(sorted_l1[i])

print(similiraty)
