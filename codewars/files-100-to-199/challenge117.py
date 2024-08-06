"""
Write a method, that will get an integer array as parameter and will process every number from this array.
Return a new array with processing every number of the input-array like this:
If the number has an integer square root, take this, otherwise square the number.
"""

import math


def square_or_square_root(arr):
    result = []
    for num in arr:
        root = math.isqrt(num)  # Compute the integer square root of num.
        if root * root == num:  # Check if num is a perfect square.
            result.append(root)
        else:
            result.append(num * num)  # Square the number if it's not a perfect square.
    return result
  
