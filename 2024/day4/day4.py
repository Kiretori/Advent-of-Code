import numpy as np

with open("day4/input4.txt", "r") as f:
    adv_input = f.readlines()

matrix = np.array([list(line.strip()) for line in adv_input])
shape = matrix.shape[0]


def check_around(mat, i, j, shape):
    xmas_count = 0
    if j + 3 < shape:
        if mat[i,j+1] + mat[i,j+2] + mat[i,j+3] == "MAS":  # --->
            xmas_count += 1

    if j - 3 >= 0:
        if mat[i, j-1] + mat[i,j-2] + mat[i,j-3] == "MAS": # <---
            xmas_count += 1

    if i + 3 < shape:
        if mat[i+1, j] + mat[i+2, j] + mat[i+3, j] == "MAS": # up
            xmas_count += 1

    if i - 3 >= 0:
        if mat[i-1, j] + mat[i-2, j] + mat[i-3, j] == "MAS":  # down
            xmas_count += 1

    if i + 3 < shape and j + 3 < shape:
        if mat[i+1, j+1] + mat[i+2, j+2] + mat[i+3, j+3] == "MAS":  # ↘
            xmas_count += 1

    if i - 3 >= 0 and j - 3 >= 0:
        if mat[i-1, j-1] + mat[i-2, j-2] + mat[i-3, j-3] == "MAS":  # ↖
            xmas_count += 1

    if i - 3 >= 0 and j + 3 < shape:
        if mat[i-1, j+1] + mat[i-2, j+2] + mat[i-3, j+3] == "MAS":  # ↙
            xmas_count +=1

    if i + 3 < shape and j - 3 >= 0:
        if mat[i+1, j-1] + mat[i+2, j-2] + mat[i+3, j-3] == "MAS":  # ↗
            xmas_count += 1

    return xmas_count
    

def is_valid_x(i, j, shape):
    return i + 1 < shape and i - 1 >= 0 and j + 1 < shape and j - 1 >= 0  




xmas_count = 0
for i in range(shape):
    for j in range(shape):
        if matrix[i,j] == "X":
            xmas_count += check_around(matrix, i, j, shape)


def check_x(mat, i, j):
    x_string = mat[i-1,j-1] + mat[i+1,j+1] + mat[i-1,j+1] + mat[i+1,j-1]
    return x_string in ["MSMS", "SMSM", "SMMS", "MSSM"]

    
cross_mas_count = 0
for i in range(1, shape-1):
    for j in range(1, shape-1):
        if matrix[i, j] == "A":
            cross_mas_count += int(check_x(matrix, i, j))
            
print(xmas_count)
print(cross_mas_count)