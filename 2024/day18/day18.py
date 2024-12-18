import numpy as np
import heapq
from tqdm import tqdm

with open("day18/input18.txt", "r") as f:
    adv_input = f.readlines()

coordinates = [(int(line.split(",")[1]), int(line.split(",")[0])) for line in adv_input]


def simulate_bytes(coordinates, n = 0):
    if n == 0:
        n = len(coordinates)
    max_x = max([coord[0] for coord in coordinates])
    max_y = max([coord[1] for coord in coordinates])
    grid = np.full(shape=(max_x + 1, max_y + 1), fill_value=".")
    for i in range(n):
        x, y = coordinates[i]
        grid[x, y] = "#"

    return grid


def djikstra(grid, start, end): 
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    pq = []
    heapq.heappush(pq, (0, start[0], start[1]))
    visited = np.full(shape = grid.shape, fill_value=np.inf)

    while pq:
        steps, x, y = heapq.heappop(pq)
        if (x, y) == end:
            return steps
        
        for (dx, dy) in directions:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1]) or grid[nx, ny] == "#":
                continue

            new_steps = steps
            new_steps += 1

            if visited[nx, ny] > new_steps:
                visited[nx, ny] = new_steps
                heapq.heappush(pq, (new_steps, nx, ny))

    return -1


def part1(coordinates):
    grid = simulate_bytes(coordinates, 1024)
    end = grid.shape[0] - 1, grid.shape[1] - 1
    return djikstra(grid, (0,0), end)


print(part1(coordinates))


def part2(coordinates):
    start_at = 1024

    initial = coordinates[:start_at]
    remaining = coordinates[start_at:]

    left, right = 0, len(coordinates) - 1
    last_working = start_at

    while left <= right:
        mid = (left + right) // 2
        current_coordinates = initial + remaining[: mid + 1]

        r = djikstra(simulate_bytes(current_coordinates), (0,0), (71, 71))

        if r != -1:
            left = mid + 1
            last_working = mid + start_at 
        else:
            right = mid - 1

    row, col = coordinates[last_working + 1]
    return f"{col},{row}"


print(part2(coordinates))
        