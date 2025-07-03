"""
Write a simple regex to validate a username.

Allowed characters are: lowercase letters, numbers, underscore.

Length should be between 4 and 16 characters (both included).
"""

import re


def validate_usr(username):
    # Regex:
    # ^                  # Start of the string.
    # [a-z0-9_]          # Allows lowercase letters (a-z), numbers (0-9), and underscore (_).
    # {4,16}             # Ensures the length is between 4 and 16 characters, inclusive.
    # $                  # End of the string.
    return re.match(r"^[a-z0-9_]{4,16}$", username) is not None
