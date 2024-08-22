"""
Given an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?
Input may be any positive or negative integer (including 0).
You can assume that all inputs are valid integers.
"""


def round_to_next5(n):
    return ((n + 4) // 5) * 5
