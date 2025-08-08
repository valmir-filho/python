"""
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
"""


def digitize(number):
    return [int(digit) for digit in str(number)][::-1]
