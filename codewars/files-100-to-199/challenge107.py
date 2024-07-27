"""
Write a function that takes a string and outputs a
strings of 1's and 0's where vowels become 1's and
non-vowels become 0's.

All non-vowels including non alpha characters (spaces,commas etc.)
should be included.
"""


def vowel_one(s):
    # Define a set of vowels for easy lookup.
    vowels = set('aeiouAEIOU')
    
    # Use a list comprehension to convert each character.
    result = ''.join('1' if char in vowels else '0' for char in s)
    
    return result
