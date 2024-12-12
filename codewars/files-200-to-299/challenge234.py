"""
In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

Create as many "shufflings" as you can!
"""

from itertools import permutations as perm


def permutations(s):
    # Use itertools.permutations to generate all permutations of the input string.
    all_permutations = set(perm(s))  # Use a set to automatically remove duplicates.
    
    # Convert the tuples back to strings and return as a list.
    return [''.join(p) for p in all_permutations]
