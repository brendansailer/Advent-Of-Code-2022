#!/usr/bin/env python3

# Save time and space
import sys
import heapq

largest = []
running_total = 0

for line in sys.stdin:
    if line == '\n':
        heapq.heappush(largest, running_total)
        running_total = 0

        # Don't let the heap have more than 3 elements
        if len(largest) >= 4:
            heapq.heappop(largest)
    else:
        running_total += int(line.strip())

print(sum(largest))

# Brute force
'''
import sys

largest = []
running_total = 0

for line in sys.stdin:
    if line == '\n':
        largest.append(running_total)
        running_total = 0
    else:
        running_total += int(line.strip())

print(sum(sorted(largest)[len(largest)-3:]))
'''
