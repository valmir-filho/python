"""
Write a function that accepts a string, and returns true if it is in the form of a phone number.

Assume that any integer from 0-9 in any of the spots will produce a valid phone number.

Only worry about the following format: (123) 456-7890 (don't forget the space after the close parentheses).
"""

import re


def valid_phone_number(phone_number):
    """
    Checks if a string is in the format of a valid phone number: (XXX) XXX-XXXX.

    Args:
        phone_number: The string to check.

    Returns:
        True if the string is a valid phone number, False otherwise.
    """
    pattern = r"^\(\d{3}\) \d{3}-\d{4}$"
    return bool(re.match(pattern, phone_number))
