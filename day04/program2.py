#!/usr/bin/env python3

import sys

count = 0

for line in sys.stdin:
    elf1, elf2 = line.strip().split(',')
    start1, end1 = map(int, elf1.split('-'))
    start2, end2 = map(int, elf2.split('-'))
    
    if start2 >= start1 and start2 <= end1:
        count += 1
        continue

    if start1 >= start2 and start1 <= end2:
        count += 1
        continue

print(count)