with open("day5/input5.txt", "r") as f:
    adv_input = f.read()

id_ranges_str, ingredients_str = adv_input.split("\n\n")

id_ranges = [(int(x), int(y)) for line in id_ranges_str.split("\n") for x, y in [line.strip().split('-')]]

ingredients = list(map(lambda x: int(x), ingredients_str.split("\n")))

# Part 1

result = 0

for id in ingredients:
    for x, y in id_ranges:
        if x <= id <= y:
            result += 1
            break

print(result)

# Part 2

def merge_ranges(ranges):
    ranges = sorted(ranges, key=lambda x: x[0])

    merged = []
    for start, end in ranges:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    
    return [tuple(r) for r in merged]

merged_id_ranges = merge_ranges(id_ranges)

result = 0

for id_range in merged_id_ranges:
    result += id_range[1] - id_range[0] + 1

print(result)
