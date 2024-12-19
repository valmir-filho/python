"""
This is a spin off of my first kata.

You are given a string containing a sequence of character sequences separated by commas.

Write a function which returns a new string containing the same character sequences except the first and the last ones but this time separated by spaces.

If the input string is empty or the removal of the first and last items would cause the resulting string to be empty, return an empty value (represented as a generic value NULL in the examples below).
"""


def array(string):
    # Split the input string into a list of items separated by commas.
    items = string.split(',')
    
    # Check if there are enough items to remove the first and last ones.
    if len(items) <= 2:
        return None
    
    # Remove the first and last items and join the rest with spaces.
    return ' '.join(items[1:-1])
