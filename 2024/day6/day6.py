import numpy as np

with open("day6/input6.txt", "r") as f:
    adv_input = f.readlines()

matrix = np.array([list(line.strip()) for line in adv_input])
shape = matrix.shape[0]

 

initial_guard = {"x": 0, "y": 0, "direction": (0,0)}
guard = {"x": 0, "y": 0, "direction": (0,0)}


for i in range(shape):
    for j in range(shape):
        if matrix[i,j] == '^':
            initial_guard["x"], initial_guard["y"] = i, j
            initial_guard["direction"] = (-1, 0)

guard = initial_guard.copy()


def check_front(guard, matrix):
    x, y = guard["x"], guard["y"]
    direction = guard["direction"]
    if matrix[x + direction[0], y + direction[1]] == "#":
        guard["direction"] = (direction[1], -direction[0])
        new_direction = guard["direction"]
        if matrix[x + new_direction[0], y+new_direction[1]] == "#":
            guard["direction"] = (new_direction[1], -new_direction[0])

    

step_count = 0
visited = np.zeros((shape, shape), dtype=bool) 
while (0 < guard["x"] < shape - 1) and (0 < guard["y"] < shape - 1):
    check_front(guard, matrix)

    if not visited[guard["x"], guard["y"]]:
        step_count += 1
        visited[guard["x"], guard["y"]] = True

    guard["x"] += guard["direction"][0]
    guard["y"] += guard["direction"][1]

visited[guard["x"], guard["y"]] = True
            
print(f"part 1: {step_count + 1}")

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def check_for_loop(loop_guard, new_matrix, init_x, init_y):
    seen = np.zeros((shape, shape, 4), dtype=bool) 
    while (0 < loop_guard["x"] < shape - 1) and (0 < loop_guard["y"] < shape - 1):
        check_front(loop_guard, new_matrix)
        

        direction_index = directions.index(loop_guard["direction"])

        if seen[loop_guard["x"], loop_guard["y"], direction_index]:
            print(f"found loop due to obstacle at: {(init_x, init_y)}")
            return True
        
            
        seen[loop_guard["x"], loop_guard["y"], direction_index] = True

        loop_guard["x"] += loop_guard["direction"][0]
        loop_guard["y"] += loop_guard["direction"][1]

    return False



loop_count = 0

print(visited)

new_matrix = matrix.copy()
for i in range(shape):
    for j in range(shape):
        if (matrix[i,j] == "^"):
            continue
        if visited[i,j]:
            if new_matrix[i,j] == ".":
                new_matrix[i,j] = "#"
                guard2 = initial_guard.copy()

                new_matrix[i, j] = "#"
                if check_for_loop(guard2, new_matrix, i, j):
                    loop_count += 1

                new_matrix[i,j] = "."

print(loop_count)