import numpy as np
import heapq
from itertools import product


with open("day16/input16.txt", "r") as f:
    adv_input = f.readlines()

grid = np.array([list(line.strip()) for line in adv_input])
shape = grid.shape[0]

def get_start_end(grid):
    for x, y in product(range(shape), range(shape)):
        if grid[x, y] == "S":
            start = (x, y)
        elif grid[x, y] == "E":
            end = (x, y)

    return start, end

def djikstra(grid, start, end): 
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    pq = []
    heapq.heappush(pq, (0, start[0], start[1], 3))
    visited = np.full(shape = (shape, shape, 4), fill_value=np.inf)

    while pq:
        score, x, y, current_dir = heapq.heappop(pq)
        if (x, y) == end:
            return score
        
        for dir_idx, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if grid[nx, ny] == "#":
                continue

            new_score = score
            new_score += 1
            if current_dir != dir_idx:
                new_score += 1000

            if visited[nx, ny, dir_idx] > new_score:
                visited[nx, ny, dir_idx] = new_score
                heapq.heappush(pq, (new_score, nx, ny, dir_idx))

    return -1

def part1(grid):
    start, end = get_start_end(grid)
    
    return djikstra(grid, start, end)


print(f"Part 1: {part1(grid)}")



def dijkstra_all_paths(grid, start, end):

    visited = np.full((shape, shape, 4), np.inf) 
    predecessor = np.empty((shape, shape, 4), dtype=object)  
    for i in range(shape):
        for j in range(shape):
            for d in range(4):
                predecessor[i, j, d] = []

    pq = []
    for d in range(4): 
        heapq.heappush(pq, (0, start[0], start[1], d))
        visited[start[0], start[1], d] = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        current_cost, x, y, direction = heapq.heappop(pq)

        if visited[x, y, direction] < current_cost:
            continue

        for new_direction, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if grid[nx, ny] != '#':  
                turn_cost = 1000 if new_direction != direction else 0
                new_cost = current_cost + 1 + turn_cost

                if new_cost < visited[nx, ny, new_direction]:
                    visited[nx, ny, new_direction] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny, new_direction))
                    predecessor[nx, ny, new_direction] = [(x, y, direction)]
                elif new_cost == visited[nx, ny, new_direction]:
                    predecessor[nx, ny, new_direction].append((x, y, direction))

    min_cost = np.inf
    best_dirs = []
    for d in range(4):
        if visited[end[0], end[1], d] < min_cost:
            min_cost = visited[end[0], end[1], d]
            best_dirs = [d]
        elif visited[end[0], end[1], d] == min_cost:
            best_dirs.append(d)

    if min_cost == np.inf:
        return [], None 

    def backtrack_paths(x, y, direction):
        if (x, y) == start:
            return [[(x, y)]]  

        all_paths = []
        for px, py, pd in predecessor[x, y, direction]:
            sub_paths = backtrack_paths(px, py, pd)
            for path in sub_paths:
                all_paths.append(path + [(x, y)])

        return all_paths

    all_paths = []
    for d in best_dirs:
        all_paths.extend(backtrack_paths(end[0], end[1], d))

    return all_paths, min_cost


def part2(grid):
    start, end = get_start_end(grid)
    paths, _ = dijkstra_all_paths(grid, start, end)

    cells_in_path = [(x,y) for path in paths for (x,y) in path]

    return len(set(cells_in_path))

print(f"Part 2: {part2(grid)}")