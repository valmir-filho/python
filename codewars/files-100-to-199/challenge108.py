"""
You might know some pretty large perfect squares. But what about the NEXT one?
Complete the findNextSquare method that finds the next integral perfect square
after the one passed as a parameter. Recall that an integral perfect square is
an integer n such that sqrt(n) is also an integer.
If the argument is itself not a perfect square then return either -1 or an empty
value like None or null, depending on your language. You may assume the argument
is non-negative.
"""

import math


def find_next_square(sq):
    # Check if the given number is a perfect square.
    root = math.sqrt(sq)
    if root.is_integer():
        # If it is a perfect square, compute the next one.
        next_root = int(root) + 1
        return next_root ** 2
    else:
        # If it's not a perfect square, return -1.
        return -1
