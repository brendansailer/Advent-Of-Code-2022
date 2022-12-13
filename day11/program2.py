#!/usr/bin/env python3

from collections import deque
import sys
import numpy as np

class Monkey:
    def __init__(self, id, items, operation, divider, true, false):
        self.id          = id
        self.items       = items
        self.operation   = operation
        self.divider   = divider
        self.true        = true
        self.false       = false
        self.inspections = 0
    
    def process(self, divider):
        old        = self.items.popleft()
        new_item   = eval(self.operation, {}, {'old': old}) % divider
        new_monkey = self.true if new_item % self.divider == 0 else self.false
        self.inspections += 1
        return new_monkey, new_item

    def __str__(self):
        return f'Monkey {self.id}: {", ".join(map(str, self.items))} [{self.inspections}]'

def simulate_monkeys(monkeys, rounds, divider):
    for round in range(1, rounds + 1):
        for monkey in monkeys:
            count = 0
            while monkey.items:
                new_monkey, new_item = monkey.process(divider)
                monkeys[new_monkey].items.append(new_item)
                count += 1

        print(f'Round {round}')
        #print_monkeys(monkeys)

def read_monkies():
    monkeys = []
    id = 0
    for monkey in sys.stdin.read().split('\n\n'):
        details   = monkey.split('\n')[1:]
        items     = deque(map(int, details[0].split(':')[-1].split(',')))
        operation = details[1].split('=')[-1]
        divider = int(details[2].strip().split()[3])
        true      = int(details[3].strip().split()[5])
        false     = int(details[4].strip().split()[5])

        monkeys.append(Monkey(id, items, operation, divider, true, false))
        id += 1

    return monkeys

def print_monkeys(monkeys):
    for monkey in monkeys:
        print(monkey)

def main():
    monkeys = read_monkies()
    divider = np.lcm.reduce([m.divider for m in monkeys])
    simulate_monkeys(monkeys, 10000, divider)
    top_monkeys = sorted(monkeys, key=lambda m: m.inspections)[-2:]
    print(top_monkeys[0].inspections * top_monkeys[1].inspections)

if __name__ == '__main__':
    main()