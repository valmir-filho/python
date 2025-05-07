"""
Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)
Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.
"""


def reverse_number(n):
    sign = -1 if n < 0 else 1
    reversed_str = str(abs(n))[::-1]
    return sign * int(reversed_str)
