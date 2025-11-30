"""
Your job is to write a function which increments a string, to create a new string.
If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
"""

import re


def increment_string(strng):
    # Use a regular expression to find the trailing number, if any.
    match = re.search(r'(\d+)$', strng)
    if match:
        # If a trailing number is found, increment it.
        number = match.group(0)
        new_number = str(int(number) + 1).zfill(len(number))
        return strng[:match.start()] + new_number
    else:
        # If no trailing number, append '1'.
        return strng + '1'
