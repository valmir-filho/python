"""
Write a function largest_n_digit_number that takes a potentially 75-digit number (represented as a string) and a
length for the input and returns the maximum integer (as a string because it can be large) that can be created from
the digits without changing the order of the digits. The given string will contain only digits 1-9.

N will always be less than or equal to the length of the string of digits.

Credit to Advent of Code 2025, Day 3.
"""


def largest_n_digit_number(seq, n):
    to_remove = len(seq) - n
    stack = []

    for digit in seq:
        while to_remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    return ''.join(stack[:n])
