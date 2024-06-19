"""
Given n, take the sum of the digits of n.
If that value has more than one digit,
continue reducing in this way until a
single-digit number is produced.
The input will be a non-negative integer.
"""


def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n
