#!/usr/bin/env python3

import sys
import heapq

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def read_input():
    return [[char for char in line.strip()] for line in sys.stdin]

def get_positions(graph):
    starts, end = [], (0,0)
    for r in range(len(graph)):
        for c in range(len(graph[0])):
            if graph[r][c] == 'S':
                graph[r][c] = 'a'
                starts.append((r, c))
            elif graph[r][c] == 'a':
                starts.append((r, c))
            elif graph[r][c] == 'E':
                end = (r, c)

    return starts, end

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
    starts, end = get_positions(graph)

    graph[end[0]][end[1]] = 'z' # Update the end location value
    steps = [dijstras(graph, start, end, len(graph), len(graph[0])) for start in starts]
    pruned_steps = [step if step != -1 else float('inf') for step in steps]
    print(f'Result: {min(pruned_steps)}')

if __name__ == '__main__':
    main()
