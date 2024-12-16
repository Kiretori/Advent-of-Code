import numpy as np
from itertools import product

with open("day15/input15.txt", "r") as f:
    adv_input = f.read()

grid, steps_list = adv_input.split("\n\n")
step_lines = steps_list.splitlines()
steps = ""
for line in step_lines:
    steps += line.strip()


grid = np.array([list(line.strip()) for line in grid.splitlines()])
grid2 = grid.copy()
shape = grid.shape[0]


directions = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}


def next_step(grid, current_pos, step):
    x, y = current_pos
    dx, dy = directions[step]
    nx, ny = x + dx, y + dy

    if grid[nx, ny] == "#":
        return (x, y)
    elif grid[nx, ny] == "O":
        next_block_pos = next_step(grid, (nx, ny), step)
        if next_block_pos != (nx, ny):
            grid[nx, ny] = grid[x, y]
            grid[x, y] = "."
            return (nx, ny)
        else:
            return (x, y)
    elif grid[nx, ny] == ".":
        grid[nx, ny] = grid[x, y]
        grid[x, y] = "."
        return (nx, ny)

def part1(grid, steps):
    for i, j in product(range(shape), range(shape)):
        if grid[i, j] == "@":
            init_pos = (i, j)
    current_pos = init_pos
    for step in steps:
        current_pos = next_step(grid, current_pos, step)

    result = 0

    for x, y in product(range(shape), range(shape)):
        if grid[x, y] == "O":
            result += 100 * x + y

    return result



print(f"Part 1: {part1(grid, steps)}")

# PART 2

def enhance_grid(grid):
    big_grid = np.zeros(shape=(shape, shape*2), dtype=str)

    for i in range(shape):
        count = 0
        for j in range(shape):
            if grid[i,j] == "@":
                big_grid[i, j + count], big_grid[i, j + 1 + count] = "@", "."
            elif grid[i,j] == "O":
                big_grid[i, j + count], big_grid[i, j + 1 + count] = "[", "]"
            else:
                big_grid[i, j + count], big_grid[i, j + 1 + count] = grid[i, j], grid[i, j]
            count += 1
    return big_grid

def next_step_p2(grid, current_pos, step):
    x, y = current_pos
    dx, dy = directions[step]
    nx, ny = x + dx, y + dy
  
    if step == "<" or step == ">":
        if grid[nx, ny] == "#":
            return (x, y)
        elif grid[nx, ny] == ".":
            grid[nx, ny] = grid[x, y]
            grid[x, y] = "."
            return (nx, ny)
        elif grid[nx, ny] in {"[", "]"}:
            next_block_pos = next_step_p2(grid, (nx, ny), step)
            if next_block_pos != (nx, ny):
                grid[nx, ny] = grid[x, y]
                grid[x, y] = "."
                return (nx, ny)
            else:
                return (x, y)
            
    else:
        if grid[nx, ny] == "#":
            return (x, y)
        elif grid[nx, ny] == ".":
            grid[nx, ny] = grid[x, y]
            grid[x, y] = "."
            return (nx, ny)
        elif grid[nx, ny] == "]":
            #right_bracket_pos = grid[nx, ny + 1]
            cells_to_check = (nx + dx, ny - 2), (nx + dx, ny - 1), (nx + dx, ny), (nx + dx, ny + 1)
            checked_brackets = []
            visited = set()
            is_possible, brackets_to_move = check_cells(grid, cells_to_check, step, (nx, ny),checked_brackets, visited)
            if is_possible:
                brackets_to_move.append({"type": "]", "pos": (nx, ny)})
                brackets_to_move.append({"type": "[", "pos": (nx, ny - 1)})
                for bracket in brackets_to_move:
                    b_x, b_y = bracket["pos"]
                    b_type = bracket["type"]
                    grid[b_x + dx, b_y + dy] = b_type
                    grid[b_x, b_y] = "." 
                grid[nx, ny] = "@"
                grid[x, y] = "."
                return (nx, ny)
            else:
                return (x, y)
        elif grid[nx, ny] == "[":
            #right_bracket_pos = grid[nx, ny + 1]
            cells_to_check = (nx + dx, ny - 1), (nx + dx, ny ), (nx + dx, ny + 1), (nx + dx, ny + 2)
            checked_brackets = []
            visited = set()
            is_possible, brackets_to_move = check_cells(grid, cells_to_check, step, (nx, ny),checked_brackets, visited)
            if is_possible:
                brackets_to_move.append({"type": "[", "pos": (nx, ny)})
                brackets_to_move.append({"type": "]", "pos": (nx, ny + 1)})
                for bracket in brackets_to_move:
                    b_x, b_y = bracket["pos"]
                    b_type = bracket["type"]
                    grid[b_x + dx, b_y + dy] = b_type
                    grid[b_x, b_y] = "." 
                grid[nx, ny] = "@"
                grid[x, y] = "."
                return (nx, ny)
            else:
                return (x, y)


def check_cells(grid, cells, step, current_pos, checked_brackets, visited):
    cx, cy = current_pos
    dx, _ = directions[step]
    current_bracket_type = grid[current_pos] 

    if current_bracket_type == "]":
        if grid[(cx + dx, cy)] + grid[(cx + dx, cy - 1)] == "..":
            checked_brackets.append({"type": grid[cx, cy],"pos":(cx, cy)})
            checked_brackets.append({"type": grid[cx, cy - 1],"pos":(cx, cy - 1)})
            visited.add((cx, cy))
            visited.add((cx, cy - 1))
            return True, checked_brackets
        elif "#" in grid[(cx + dx, cy)] + grid[(cx + dx, cy - 1)]:
            return False, None
    else:
        if grid[(cx + dx, cy)] + grid[(cx + dx, cy + 1)] == "..":
            checked_brackets.append({"type": grid[cx, cy],"pos":(cx, cy)})
            checked_brackets.append({"type": grid[cx, cy + 1],"pos":(cx, cy + 1)})
            visited.add((cx, cy))
            visited.add((cx, cy + 1))
            return True, checked_brackets
        elif "#" in grid[(cx + dx, cy)] + grid[(cx + dx, cy + 1)]:
            return False, None
        

    for cell in cells:
        x, y = cell
        if cell in visited:
            continue
        if current_bracket_type == "]":
            if grid[cell] == "]" and cy - 1 <= y <= cy + 1:
                cells_to_check = (x + dx, y - 2), (x + dx, y - 1), (x + dx, y), (x + dx, y + 1)   
                if not check_cells(grid, cells_to_check, step, (x,y), checked_brackets, visited)[0]:
                    return False, None 
                checked_brackets.append({"type": "]", "pos": cell})
                checked_brackets.append({"type": "[","pos": (cell[0], cell[1]-1)})
                visited.add(cell)
                visited.add((cell[0], cell[1]-1))

            elif grid[cell] == "[" and cy - 2 <= y <= cy:
                cells_to_check = (x + dx, y - 1), (x + dx, y), (x + dx, y + 1), (x + dx, y + 2)   
                if not check_cells(grid, cells_to_check, step, (x,y), checked_brackets, visited)[0]:
                    return False, None 
                checked_brackets.append({"type": "[", "pos": cell})
                checked_brackets.append({"type": "]","pos": (cell[0], cell[1]+1)}) 
                visited.add(cell)
                visited.add((cell[0], cell[1]+1))

        elif current_bracket_type == "[":
            if grid[cell] == "]" and cy <= y <= cy + 2:
                cells_to_check = (x + dx, y - 2), (x + dx, y - 1), (x + dx, y), (x + dx, y + 1)   
                if not check_cells(grid, cells_to_check, step, (x,y), checked_brackets, visited)[0]:
                    return False, None 
                checked_brackets.append({"type": "]", "pos": cell})
                checked_brackets.append({"type": "[","pos": (cell[0], cell[1]-1)})
                visited.add(cell)
                visited.add((cell[0], cell[1]-1))

            elif grid[cell] == "[" and cy - 1 <= y <= cy + 1:
                cells_to_check = (x + dx, y - 1), (x + dx, y), (x + dx, y + 1), (x + dx, y + 2)   
                if not check_cells(grid, cells_to_check, step, (x,y), checked_brackets, visited)[0]:
                    return False, None 
                checked_brackets.append({"type": "[", "pos": cell})
                checked_brackets.append({"type": "]","pos": (cell[0], cell[1]+1)}) 
                visited.add(cell)
                visited.add((cell[0], cell[1]+1))
        
    
    return True, checked_brackets

def part2(grid, steps):
    big_grid = enhance_grid(grid)
    for i, j in product(range(shape), range(2*shape)):
        if big_grid[i, j] == "@":
            init_pos = (i, j)
    current_pos = init_pos

    for i, step in enumerate(steps):
        
        current_pos = next_step_p2(big_grid, current_pos, step)

    result = 0
    for i, j in product(range(shape), range(2*shape)):
        if big_grid[i, j] == "[":
            result += 100 * i + j

    return result
    

print(f"Part 2: {part2(grid2, steps)}")