#!/usr/bin/env python3

import sys

buffer = sys.stdin.read().strip()

for i in range(0, len(buffer)-14):
    if len(set(buffer[i:i+14])) == 14:
        print(i+14)
        break

print(-1)