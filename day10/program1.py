#!/usr/bin/env python3

import sys
import collections

MEASURE_POINTS = [20, 60, 100, 140, 180, 220]

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

def calculate_results(values):
    signal_strength_sum = 0
    for cycle in MEASURE_POINTS:
        signal_strength_sum += cycle*values[cycle]

    return signal_strength_sum

def main():
    values = replay_instructions()
    print(calculate_results(values))

if __name__ == '__main__':
    main()