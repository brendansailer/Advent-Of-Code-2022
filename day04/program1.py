#!/usr/bin/env python3

import sys

count = 0

for line in sys.stdin:
    elf1, elf2 = line.strip().split(',')
    start1, end1 = map(int, elf1.split('-'))
    start2, end2 = map(int, elf2.split('-'))

    if start1 <= start2 and end2 <= end1:
        count += 1
        print(start1, end1, start2, end2)
        continue
    
    if start2 <= start1 and end1 <= end2:
        count += 1
        print(start1, end1, start2, end2)
        continue

print(count)