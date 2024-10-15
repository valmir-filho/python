"""
Write a method (or function, depending on the language) that converts a string to camelCase,
that is, all words must have their first letter capitalized and spaces must be removed.
"""


def camel_case(s):
    # Split the string into words, capitalize each word, and join them without spaces.
    return ''.join(word.capitalize() for word in s.split())
