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

    def dfs(start, char):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        region_cells = []
        stack = [start]  # Use a stack instead of a queue

        while stack:
            x, y = stack.pop()  # Pop from the top of the stack

            # Check bounds, visited, and character condition
            if not (0 <= x < shape and 0 <= y < shape) or visited[x, y] or matrix[x, y] != char:
                continue

            visited[x, y] = True
            region_cells.append((x, y))

            for dx, dy in directions:
                stack.append((x + dx, y + dy))  # Add neighboring cells to the stack

        return region_cells
    

    for i, j in product(range(shape), range(shape)):
        if not visited[i, j]:
            char = matrix[i, j]
            region_cells = dfs((i,j), char)
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

def count_borders(matrix, regions):
    rows, cols = matrix.shape
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    direction_names = ["up", "down", "left", "right"]

    def get_border_segments(region_cells, region_char):
        border_segments = set()
        for x, y in region_cells:
            for d, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy

                if not (0 <= nx < rows and 0 <= ny < cols) or matrix[nx, ny] != region_char:
                    segment = ((x, y), direction_names[d])
                    border_segments.add(segment)
        return border_segments

    def group_borders(border_segments):
        visited = set()
        borders = 0

        def dfs(segment):
            stack = deque([segment])
            while stack:
                current_segment = stack.pop()
                if current_segment in visited:
                    continue
                visited.add(current_segment)
                x, y = current_segment[0]
                direction = current_segment[1]

                for (dx, dy) in directions:
                    nx, ny = x + dx, y + dy
                    next_segment = ((nx, ny), direction)
                    if next_segment in border_segments and next_segment not in visited:
                        stack.append(next_segment)

        for segment in border_segments:
            if segment not in visited:
                dfs(segment)
                borders += 1
        return borders

    border_counts = {}

    for region_id, region in regions.items():
        region_char = region["Label"]
        region_cells = region["Cells"]

        border_segments = get_border_segments(region_cells, region_char)

        borders_for_region = group_borders(border_segments)
        border_counts[region_id] = borders_for_region

    return border_counts



area_per_id = {}
for id, region in regions.items():
    area_per_id[id] = len(region["Cells"])

print(area_per_id)
borders_per_id = count_borders(matrix, regions)

sum_p2 = 0
for id in area_per_id:
    sum_p2 += area_per_id[id] * borders_per_id[id]

print(sum_p2)