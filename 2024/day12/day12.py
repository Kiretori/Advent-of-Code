from collections import deque
from itertools import product
import numpy as np

with open("day12/input12.txt", "r") as f:
    adv_input = f.readlines()

matrix = np.array([list(line.strip()) for line in adv_input])
shape = matrix.shape[0]


def get_regions(matrix):
    visited = np.zeros(shape=(shape, shape), dtype=bool)
    regions = {}
    region_id = 0

    def bfs(start, char):

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        region_cells = []
        queue = deque([start])
       

        while queue:
            x, y = queue.popleft()
        
            if not (0 <= x < shape and 0 <= y < shape) or visited[x,y] or matrix[x,y] != char:
                continue
            
            visited[x, y] = True
            region_cells.append((x, y))
            for dx, dy in directions:
                queue.append((x + dx, y + dy))
        
        return region_cells
    

    for i, j in product(range(shape), range(shape)):
        if not visited[i, j]:
            char = matrix[i, j]
            region_cells = bfs((i,j), char)
            regions[region_id] = {"Label": char, "Cells": region_cells} 
            region_id += 1


    return regions


def get_areas(regions):

    return [len(region['Cells']) for region in regions.values()]
        


def get_perimeters(matrix, regions):
    perimeters = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for id, region in regions.items():
        perimeter = 0
        char = region["Label"]

        for x, y in region["Cells"]:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < shape and 0 <= ny < shape) or matrix[nx,ny] != char:
                    perimeter += 1

        perimeters.append(perimeter)

    return perimeters

regions = get_regions(matrix)

areas, perimeters = get_areas(regions), get_perimeters(matrix, regions)


total_price = sum([pair[0] * pair[1] for pair in zip(areas, perimeters)])

print(total_price)


# Part 2 


def get_regions_with_sides(matrix):
    visited = np.zeros(shape=(shape, shape), dtype=bool)
    regions = {}
    region_id = 0

    def bfs(start, char):

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        region_cells = []
        queue = deque([start])

        sides = 0
       
        prev_cell = None
        while queue:
            x, y = queue.popleft()
        
            if not (0 <= x < shape and 0 <= y < shape) or visited[x,y] or matrix[x,y] != char:
                continue
            
            visited[x, y] = True
            region_cells.append((x, y))

            if prev_cell is not None:
                # If the current cell is not adjacent to the previous cell in a straight line
                if abs(x - prev_cell[0]) + abs(y - prev_cell[1]) > 1:
                    sides += 1
            
            prev_cell = (x, y)

            for dx, dy in directions:
                queue.append((x + dx, y + dy))
        
        if len(region_cells) == 1: sides = 4

        return region_cells, sides
    

    for i, j in product(range(shape), range(shape)):
        if not visited[i, j]:
            char = matrix[i, j]
            region_cells, sides = bfs((i,j), char)
            regions[region_id] = {"Label": char, "Sides": sides, "Cells": region_cells} 
            region_id += 1


    return regions


print(get_regions_with_sides(matrix))