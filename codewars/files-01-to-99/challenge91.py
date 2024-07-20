"""
Write a function named first_non_repeating_letter† that takes a string input,
and returns the first character that is not repeated anywhere in the string.
For example, if given the input 'stress', the function should return 't', since
the letter t only occurs once in the string, and occurs first in the string.
As an added challenge, upper- and lowercase letters are considered the same character,
but the function should return the correct case for the initial letter. For example,
the input 'sTreSS' should return 'T'.
If a string contains all repeating characters, it should return an empty string ("");
Note: the function is called firstNonRepeatingLetter for historical reasons, but your
function should handle any Unicode character.
"""


def first_non_repeating_letter(s):
    # Create a dictionary to count the occurrences of each character in a case-insensitive manner.
    char_count = {}
    
    # First pass: count occurrences.
    for char in s:
        lower_char = char.lower()
        if lower_char in char_count:
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1
            
    # Second pass: find the first non-repeating character.
    for char in s:
        if char_count[char.lower()] == 1:
            return char
    
    # If no non-repeating character is found, return an empty string.
    return ""
