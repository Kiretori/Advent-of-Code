import numpy as np

with open("day8/input8.txt", "r") as f:
    adv_input = f.readlines()

matrix = np.array([list(line.strip()) for line in adv_input])
shape = matrix.shape[0]

antennas = {}

for i in range(shape):
    for j in range(shape):
        if matrix[i,j] != ".":
            if matrix[i,j] not in antennas:
                antennas[matrix[i,j]] = []
            antennas[matrix[i,j]].append((i,j))


antinodes = np.zeros(shape=(shape,shape), dtype=bool)

for antenna, positions in antennas.items():
    for pos in positions:
        for other_pos in positions:
            if other_pos != pos:
                antinode = ((2 * other_pos[0]) - pos[0], (2 * other_pos[1]) - pos[1])
                if 0 <= antinode[0] < shape and 0 <= antinode[1] < shape:  
                    antinodes[antinode] = True


print(np.sum(antinodes))

antinodes2 = np.zeros(shape=(shape,shape), dtype=bool)

for antenna, positions in antennas.items():
    for pos in positions:
        for other_pos in positions:
            if other_pos != pos:
                new_pos = pos
                antinode = other_pos
                while 0 <= antinode[0] < shape and 0 <= antinode[1] < shape:
                    other_pos = antinode
                    antinodes2[antinode] = True
                    antinode = ((2 * antinode[0]) - new_pos[0], (2 * antinode[1]) - new_pos[1]) 
                    new_pos = other_pos
                    



print(np.sum(antinodes2))