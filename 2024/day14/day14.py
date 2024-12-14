from collections import defaultdict
from PIL import Image
import numpy as np
with open("day14/input14.txt", "r") as f:
    adv_input = f.readlines()

robots = []

for line in adv_input:
    stripped_line = line.replace("p=", "").replace("v=", "").strip()
    p_str, v_str = stripped_line.split(" ")
    p = (int(p_str.split(",")[0]), int(p_str.split(",")[1]))
    v = (int(v_str.split(",")[0]), int(v_str.split(",")[1]))

    robots.append({"p": p, "v": v})

tile_robot_counts = defaultdict(int)
# x num of column, y num of row

def get_positions(robots, size_x, size_y, seconds):
    positions = []
    for robot in robots:
        p, v = robot["p"], robot["v"]
        f_x = (p[0] + seconds * v[0]) % size_x
        f_y = (p[1] + seconds * v[1]) % size_y
        positions.append((f_x, f_y))

    return positions

def get_safety_score(positions, size_x, size_y):
    top_left_q, top_right_q, bottom_left_q, bottom_right_q = 0, 0, 0, 0

    for pos in positions:
        if 0 <= pos[0] < size_x // 2 and 0 <= pos[1] < size_y // 2:
            top_left_q += 1
        elif size_x // 2 < pos[0] <= size_x - 1 and 0 <= pos[1] < size_y // 2:
            top_right_q += 1
        elif 0 <= pos[0] < size_x // 2 and size_y // 2 < pos[1] <= size_y - 1:
            bottom_left_q += 1
        elif size_x // 2 < pos[0] <= size_x - 1 and size_y // 2 < pos[1] <= size_y - 1 :
            bottom_right_q += 1

    return top_left_q * top_right_q * bottom_left_q * bottom_right_q


def solve_part1(size_x, size_y, seconds):
    return get_safety_score(get_positions(robots, size_x, size_y, seconds), size_x, size_y)


print(solve_part1(101, 103, 100))



