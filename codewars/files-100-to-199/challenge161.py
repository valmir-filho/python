"""
Your task is to find the nearest square number of a positive integer n.
In mathematics, a square number or perfect square is an integer that is
the square of an integer; in other words, it is the product of some integer with itself.
"""

import math


def nearest_sq(n):
    # Calculate the integer part of the square root of n.
    sqrt_n = math.isqrt(n)
    
    # Compute the nearest squares.
    square1 = sqrt_n ** 2
    square2 = (sqrt_n + 1) ** 2
    
    # Determine which square is closer to n.
    if abs(n - square1) <= abs(n - square2):
        return square1
    else:
        return square2
