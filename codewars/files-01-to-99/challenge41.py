"""
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
"""


def repeat_characters(input_string):
    repeated_string = ""
    for char in input_string:
        repeated_string += char * 2
    return repeated_string
