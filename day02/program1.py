#!/usr/bin/env python3

import sys

score = 0
OUTCOMES = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}

for line in sys.stdin:
    opponent, mine = [OUTCOMES[value] for value in line.strip().split()]

    score += mine # Add the score for what I threw
    if opponent == mine: # Draw
        score += 3
    elif opponent == 1 and mine == 2 or opponent == 2 and mine == 3 or opponent == 3 and mine == 1: # Win
        score += 6

print(score)