#!/usr/bin/env python3

import sys

largest = 0
running_total = 0

for line in sys.stdin:
    if line == '\n':
        largest = max(largest, running_total)
        running_total = 0
    else:
        running_total += int(line.strip())

print(largest)