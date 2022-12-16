#!/usr/bin/env python3

import sys
import heapq

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def read_input():
    return [[char for char in line.strip()] for line in sys.stdin]

def get_positions(graph):
    start, end = (0,0), (0,0)
    for r in range(len(graph)):
        for c in range(len(graph[0])):
            if graph[r][c] == 'S':
                start = (r, c)
            elif graph[r][c] == 'E':
                end = (r, c)

    return start, end

def dijstras(graph, start, end, len_r, len_c):
    seen = set()
    frontier = [(0, start)]

    while frontier:
        distance, vert = heapq.heappop(frontier)
        r, c = vert
        if (r, c) in seen:
            continue
        elif (r, c) == end:
            return distance

        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr >= 0 and nr < len_r and nc >= 0 and nc < len_c: # In bounds check
                to_char, from_char = ord(graph[nr][nc]), ord(graph[r][c]) # Verify the difference is at most 1
                if to_char-1 <= from_char:
                    heapq.heappush(frontier, (distance+1, (nr, nc)))

        seen.add((r, c))

    return -1

def main():
    graph = read_input()
    start, end = get_positions(graph)

    graph[start[0]][start[1]] = 'a' # Update the start and end locations to their values
    graph[end[0]][end[1]] = 'z'

    steps = dijstras(graph, start, end, len(graph), len(graph[0]))
    print(f'Result: {steps}')

if __name__ == '__main__':
    main()
