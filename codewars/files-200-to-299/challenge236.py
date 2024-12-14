"""
Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string).

Notes:
- If either input is an empty string, consider it as zero;
- Inputs and the expected output will never exceed the signed 32-bit integer limit (2^31 - 1).
"""


def sum_str(a, b):
    # Convert inputs to integers, treating empty strings as zero.
    num1 = int(a) if a else 0
    num2 = int(b) if b else 0
    # Calculate the sum and return it as a string.
    return str(num1 + num2)
