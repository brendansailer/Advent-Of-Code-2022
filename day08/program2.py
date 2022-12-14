#!/usr/bin/env python3

import functools 
import itertools
import operator
import sys

# Code taken from pbui

BORDER      = -1
DIRECTIONS  = (
    (-1,  0),   # Up
    ( 1,  0),   # Down
    ( 0, -1),   # Left
    ( 0,  1),   # Right
)

def read_grid(stream=sys.stdin):
    grid = []
    for line in stream:
        grid.append([BORDER] + list(map(int, line.strip())) + [BORDER])

    grid.insert(0, [BORDER]*len(grid[0]))
    grid.append([BORDER]*len(grid[0]))
    return grid

def count_trees_all(grid, r, c):
    return functools.reduce(operator.mul, (
        count_trees_one(grid, r + dr, c + dc, grid[r][c], dr, dc) for dr, dc in DIRECTIONS
    ))

def count_trees_one(grid, r, c, height, dr, dc):
    # Base case: hit border
    if grid[r][c] == BORDER:
        return 0

    # Base case: hit taller tree
    if grid[r][c] >= height:
        return 1

    # Recursive: keep going
    return count_trees_one(grid, r + dr, c + dc, height, dr, dc) + 1

def main():
    grid  = read_grid()
    cells = list(itertools.product(range(1, len(grid) - 1), range(1, len(grid[0]) - 1)))
    scene = max(count_trees_all(grid, r, c) for r, c in cells)
    print(f'Result: {scene}')

if __name__ == '__main__':
    main()