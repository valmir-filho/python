"""
Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.

Requirements:
- You can assume you will be given an integer input;
- You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).

NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out.
Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.
"""

import math


def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    max_divisor = int(math.sqrt(num)) + 1
    for divisor in range(3, max_divisor, 2):
        if num % divisor == 0:
            return False
    return True
