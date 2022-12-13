#!/usr/bin/env python3

import sys
import collections

SPACES = (40*6)+1

def replay_instructions():
    cycle = 1
    register_value = 1
    values = collections.defaultdict(int)

    for instruction in sys.stdin:
        values[cycle] = register_value

        if instruction.strip() == 'noop':
            cycle += 1
        else:
            _, value = instruction.strip().split()
            values[cycle+1] = register_value
            register_value += int(value)
            cycle += 2

    return values

def generate_image(values):
    for row in range(6):
        crt_screen = ""
        for col in range(40):
            cycle = (row*40) + col + 1
            if col-1 <= values[cycle] <= col+1:
                crt_screen += '#'
            else:
                crt_screen += '.'
        print(crt_screen)

def main():
    values = replay_instructions()
    generate_image(values)

if __name__ == '__main__':
    main()