from collections import deque
from itertools import product
import numpy as np

with open("day10/input10.txt", "r") as f:
    adv_input = f.readlines()

matrix = np.array([list(line.strip()) for line in adv_input])
shape = matrix.shape[0]



def bfs_search(matrix, start, target):
    rows, cols = matrix.shape
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    visited = set()
    visited.add(start)

    path_count = 0

    while queue:
        x, y = queue.popleft()

        if matrix[x][y] == target:
            path_count += 1
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if matrix[nx][ny].isdigit() and int(matrix[nx][ny]) == int(matrix[x][y]) + 1:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
    
    return path_count



zeroes = [(x, y) for (x, y) in product(range(shape), range(shape)) if matrix[x,y] == '0']


p1_sum = sum(map(lambda pair: bfs_search(matrix, (pair[0], pair[1]), '9'), zeroes))
print(p1_sum)



def bfs_count_distinct_paths(matrix, start, target):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

    queue = deque([[start]])
    distinct_paths = 0  

    while queue:
        path = queue.popleft()
        x, y = path[-1]  

        if matrix[x][y] == target:
            distinct_paths += 1
            continue  

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in path:
                if matrix[nx][ny].isdigit() and int(matrix[nx][ny]) == int(matrix[x][y]) + 1:  
                    queue.append(path + [(nx, ny)])  

    return distinct_paths

p2_sum = sum(map(lambda pair: bfs_count_distinct_paths(matrix, (pair[0], pair[1]), '9'), zeroes))
print(p2_sum)