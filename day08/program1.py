#!/usr/bin/env python3

import sys

grid = [[int(tree) for tree in line.strip()] for line in sys.stdin]

len_x, len_y = len(grid[0]), len(grid)
result = [[True for _ in range(len_x)] for _ in range(len_y)] # True = Hidden

for y in range(1, len_y):
    max_height = grid[y][0]
    for x in range(1, len_x):
        if grid[y][x] > max_height:
            result[y][x] = False
            max_height = grid[y][x]

for y in range(1, len_y):
    max_height = grid[y][-1]
    for x in range(len_x-1, -1, -1):
        if grid[y][x] > max_height:
            result[y][x] = False
            max_height = grid[y][x]

for x in range(1, len_x):
    max_height = grid[0][x]
    for y in range(1, len_y):
        if grid[y][x] > max_height:
            result[y][x] = False
            max_height = grid[y][x]

for x in range(1, len_x):
    max_height = grid[-1][x]
    for y in range(len_y-1, -1, -1):
        if grid[y][x] > max_height:
            result[y][x] = False
            max_height = grid[y][x]

count = 0
for row in result[1:-1]:
    for value in row[1:-1]:
        if value == True:
            count += 1

print(len_x, len_y, len_x*len_y)
print(count)