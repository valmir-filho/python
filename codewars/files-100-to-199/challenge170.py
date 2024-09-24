"""
Some numbers have funny properties.

For example:

89 --> 8¹ + 9² = 89 * 1
695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Given two positive integers n and p, we want to find a positive integer k,
if it exists, such that the sum of the digits of n raised to consecutive
powers starting from p is equal to k * n.
"""


def dig_pow(n, p):
    # Convert n into its digits.
    digits = [int(d) for d in str(n)]
    
    # Calculate the sum of each digit raised to successive powers.
    total_sum = sum(d ** (p + i) for i, d in enumerate(digits))
    
    # Check if the total sum is divisible by n.
    if total_sum % n == 0:
        return total_sum // n  # Return k.
    else:
        return -1  # Return -1 if no such k exists.
