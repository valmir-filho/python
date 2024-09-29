"""
Write a function named sumDigits which takes a number as
input and returns the sum of the absolute value of each
of the number's decimal digits.
"""


def sum_digits(number):
    # Convert the number to its absolute value and then to a string.
    str_number = str(abs(number))
    # Use a generator expression to sum the integer value of each digit.
    return sum(int(digit) for digit in str_number)
