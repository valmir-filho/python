"""
A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
because it uses the letters A-Z at least once (case is irrelevant).
Given a string, detect whether or not it is a pangram. Return True if it is, False if not.
Ignore numbers and punctuation.
"""


def is_pangram(s):
    # Define the alphabet set.
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    
    # Remove non-alphabetic characters and convert to lowercase.
    sanitized_string = ''.join(filter(str.isalpha, s.lower()))
    
    # Create a set of unique characters in the sanitized string.
    unique_chars = set(sanitized_string)
    
    # Check if the unique characters cover the whole alphabet.
    return unique_chars >= alphabet
