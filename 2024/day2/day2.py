with open("day2/input2.txt", "r") as f:
    adv_input = f.readlines()

            

def is_line_safe(line):
    prev_slope = 0
    is_line_safe = True
    for i in range(len(line) - 1):
        slope = line[i] - line[i+1]
        if (abs(slope) < 1) or (abs(slope) > 3):
            print(f"Difference between {line[i]} and {line[i+1]} is out of range")
            is_line_safe = False
            prev_slope = slope
            break
        if slope * prev_slope < 0:
            print(f"Slope between {line[i]} and {line[i+1]} is of opposite signs (prev: {prev_slope}, current: {slope})")
            is_line_safe = False
            prev_slope = slope
            break

        prev_slope = slope
    
    return is_line_safe


safe = 0

safe_lines = []

for line in adv_input:
    nums = line.split(" ")
    nums = [int(x) for x in nums]
    if not is_line_safe(nums):
        for i in range(len(nums)):
            sliced_nums = nums[:i] + nums[i+1:]
            if is_line_safe(sliced_nums):
                safe += 1
                break
    else:
        safe += 1


print(safe_lines)
print(safe)