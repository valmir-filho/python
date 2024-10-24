"""
Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
"""

from collections import Counter


def find_it(seq):
    # Count occurrences of each number.
    counts = Counter(seq)
    
    # Find and return the number that appears an odd number of times.
    for num, count in counts.items():
        if count % 2 != 0:
            return num
