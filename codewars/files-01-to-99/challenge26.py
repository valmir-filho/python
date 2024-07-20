"""
Write a function that takes an integer as input, and returns the number of bitsthat are
equal to one in the binary representation of that number. You can guarantee that input is
non-negative.
"""


function countBits(n):
    count = 0
    while n > 0:
        if n % 2 == 1:
            count += 1
        n = n // 2
    return count
