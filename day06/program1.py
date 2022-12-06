#!/usr/bin/env python3

import sys

buffer = sys.stdin.read().strip()

for i in range(0, len(buffer)-4):
    if len(set(buffer[i:i+4])) == 4:
        print(i+4)
        break
