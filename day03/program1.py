#!/usr/bin/env python3

import sys

priority = 0

for line in sys.stdin:
    middle = len(line.strip())//2
    first, second = set([char for char in line.strip()[:middle]]), set([char for char in line.strip()[middle:]])
    common_letter = list(first & second)[0]
    if common_letter.islower():
        priority += ord(common_letter) - 96
    else:
        priority += ord(common_letter) - 64 + 26

print(priority)