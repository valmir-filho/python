"""
Write a program to determine if a string contains only unique characters.
Return true if it does and false otherwise.

The string may contain any of the 128 ASCII characters.
Characters are case-sensitive, e.g. "a" and "A" are considered different characters.
"""


def has_unique_chars(string):
    seen_chars = set()
    for char in string:
        if char in seen_chars:
            return False
        seen_chars.add(char)
    return True
