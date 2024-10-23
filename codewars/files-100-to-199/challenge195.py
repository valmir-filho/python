"""
Given a positive number n > 1 find the prime factor decomposition of n.
The result will be a string with the following form: (p1**n1)(p2**n2)...(pk**nk), 
with the p(i) in increasing order and n(i) empty if n(i) is 1.
"""

import math


def prime_factors(n):
    factors = []
    count = 0
    
    # Check for number of 2's.
    while n % 2 == 0:
        n //= 2
        count += 1
    if count > 0:
        factors.append(f"(2**{count})" if count > 1 else "(2)")

    # Check for odd factors from 3 to sqrt(n).
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        count = 0
        while n % i == 0:
            n //= i
            count += 1
        if count > 0:
            factors.append(f"({i}**{count})" if count > 1 else f"({i})")

    # If n is a prime number greater than 2.
    if n > 2:
        factors.append(f"({n})")

    return ''.join(factors)
