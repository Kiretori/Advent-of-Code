from itertools import product
with open("day4/input4.txt", "r") as f:
    adv_input = f.readlines()


grid = [list(line.strip()) for line in adv_input]

m, n = len(grid), len(grid[0])

directions = {(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)}

# Part 1

result = 0

for x, y in product(range(m), range(n)):
    if grid[x][y] != '@':
        continue

    neighbor_count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n:
            neighbor_count += bool(grid[nx][ny] == '@')

    result += bool(neighbor_count < 4)

print(result)


# Part 2

result = 0
removed = 0

while True:
    to_remove = set()
    for x, y in product(range(m), range(n)):
        if grid[x][y] != '@':
            continue

        neighbor_count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                neighbor_count += bool(grid[nx][ny] == '@')

        if neighbor_count < 4:
            result += 1
            to_remove.add((x, y))

    for x, y in to_remove:
        grid[x][y] = '.'
    
    if len(to_remove) == 0:
        break

print(result)