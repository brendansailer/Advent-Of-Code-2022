#!/usr/bin/env python3

import sys
import re

stacks = [[] for x in range(9)]

input, directions = sys.stdin.read().split('\n\n')
input = input.split('\n')

for index in range(len(input)-2, -1, -1):
    row = input[index]
    for x in range(0, len(row), 4):
        item = row[x:x+4]
        if item[0] == '[':
            stacks[x//4].append(item[1])

for direction in directions.split('\n'):
    amount, origin, destination = map(int, re.match('move (\d*) from (\d*) to (\d*)', direction).groups())

    # Move crates
    existing = len(stacks[origin-1])
    remaining = existing - amount
    stacks[destination-1].extend(stacks[origin-1][remaining:])

    # Delete the moved crates
    for _ in range(amount):
        stacks[origin-1].pop()

print(''.join([stack[-1] for stack in stacks]))
