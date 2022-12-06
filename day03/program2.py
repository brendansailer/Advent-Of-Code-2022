#!/usr/bin/env python3

import sys

priority = 0
index    = 0

lines = sys.stdin.readlines()

while index < len(lines):
    first  = set([char for char in lines[index].strip()])
    second = set([char for char in lines[index+1].strip()])
    third  = set([char for char in lines[index+2].strip()])

    common_letter = list(first & second & third)[0]
    if common_letter.islower():
        priority += ord(common_letter) - 96
    else:
        priority += ord(common_letter) - 64 + 26

    index += 3

print(priority)