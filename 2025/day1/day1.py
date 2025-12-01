with open("day1/input1.txt", "r") as f:
    adv_input = f.readlines()

# Part 1

counter = 0
dial_pointer = 50
for line in adv_input:
    prefix = -1 if line[0] == "L" else 1
    number = int(line[1:])

    step = prefix * number
    dial_pointer += step

    if dial_pointer % 100 == 0:
        counter += 1

print(counter)


# Part 2

counter = 0
dial_pointer = 50  
for line in adv_input:
    dir = line[0]
    step = int(line[1:])

    if dir == "R":
        
        counter += (dial_pointer + step) // 100
        dial_pointer = (dial_pointer + step) % 100

    else:  
        if dial_pointer > 0:
            if step < dial_pointer:
                passes = 0
            else:
                passes = 1 + (step - dial_pointer) // 100
        else:  
            passes = step // 100

        counter += passes
        dial_pointer = (dial_pointer - step) % 100

print(counter)