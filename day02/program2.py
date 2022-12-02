#!/usr/bin/env python3

import sys

score = 0
OUTCOMES = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}

for line in sys.stdin:
    opponent, mine = [OUTCOMES[value] for value in line.strip().split()]

    if mine == 1: # Lose
        if opponent == 1:
            score += 3
        elif opponent == 2:
            score += 1
        else: 
            score += 2
    elif mine == 2: # Draw
        score += opponent # Copy them
        score += 3
    else: # Win
        score += 6
        if opponent == 1:
            score += 2
        elif opponent == 2:
            score += 3
        else: 
            score += 1

print(score)