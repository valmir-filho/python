"""
Given a string str, reverse it and omit all non-alphabetic characters.
"""


def reverse_letter(st):
    # Filter only alphabetic characters from the string.
    filtered = ''.join(char for char in st if char.isalpha())
    # Reverse the filtered string.
    reversed_str = filtered[::-1]
    return reversed_str
  
