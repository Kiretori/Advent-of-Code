import math
import time
from collections import defaultdict

with open("day11/input11.txt", "r") as f:
    adv_input = f.read()


def is_even_digits(n):
    if n == 0:
        return False 
    num_digits = math.floor(math.log10(abs(n))) + 1
    return num_digits % 2 == 0 


def split_integer(n):
    num_digits = int(math.log10(n)) + 1
    
    if num_digits % 2 != 0:
        raise ValueError("The number must have an even number of digits")

    midpoint = num_digits // 2

    divisor = 10 ** midpoint
    first_half = n // divisor  
    second_half = n % divisor 

    return first_half, second_half


def get_result(adv_input, iter):
    stones = [int(x) for x in adv_input.split()]

    stone_counts = defaultdict(int)
    for stone in stones:
        stone_counts[stone] += 1

    leftover = defaultdict(int)

    for _ in range(iter):
        
        for stone in list(stone_counts.keys()):
            count = stone_counts[stone] - leftover[stone]
            if stone == 0:
                stone_counts[stone] -= 1 * count

                stone_counts[1] += 1 * count
                leftover[1] += 1 * count 
            elif is_even_digits(stone):

                stone_counts[stone] -= 1 * count

                l, r = split_integer(stone)
                stone_counts[l] += 1 * count 
                stone_counts[r] += 1 * count
                leftover[l] += 1 * count 
                leftover[r] += 1 * count  
            else:            
                stone_counts[stone] -= 1 * count 
                stone_counts[stone * 2024] += 1 * count 
                leftover[stone * 2024] += 1 * count 

            if stone_counts[stone] == 0:
                stone_counts.pop(stone)

        leftover.clear()

    return sum(stone_counts.values())


# Part 1 

start = time.perf_counter()

print(get_result(adv_input, 25))

end = time.perf_counter()

print(f"Part 1: {(end - start):.6}s")


# Part 2 

start = time.perf_counter()

print(get_result(adv_input, 75))

end = time.perf_counter()

print(f"Part 2: {(end - start):.6}s")