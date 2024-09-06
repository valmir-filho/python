"""
Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it,
is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 points
 
A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet
(contributing to the 500 points) or as a single 50 points, but not both in the same roll.
"""

from collections import Counter


def score(dice):
    # Count occurrences of each die value.
    counts = Counter(dice)
    total_score = 0
    
    # Score for three-of-a-kind.
    if counts[1] >= 3:
        total_score += 1000
        counts[1] -= 3
    for num in [6, 5, 4, 3, 2]:
        if counts[num] >= 3:
            total_score += num * 100
            counts[num] -= 3
    
    # Score for individual 1's and 5's.
    total_score += counts[1] * 100
    total_score += counts[5] * 50

    return total_score
