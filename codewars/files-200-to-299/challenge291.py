"""
In this Kata, you will implement a function count that takes an integer and returns the number of digits in factorial(n).

For example, count(5) = 3, because 5! = 120, and 120 has 3 digits.

Brute force is not possible. A little research will go a long way, as this is a well known series.
"""

import math


def count(n):
    if n == 0 or n == 1:
        return 1
    log_sum = 0
    for i in range(2, n + 1):
        log_sum += math.log10(i)
    return math.floor(log_sum) + 1
