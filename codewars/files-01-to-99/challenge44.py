"""
An isogram is a word that has no repeating letters,
consecutive or non-consecutive. Implement a function
that determines whether a string that contains only
letters is an isogram. Assume the empty string is an isogram.
Ignore letter case.
"""


def is_isogram(word):
    # Normalize the word to lower case to ignore case differences.
    normalized_word = word.lower()
    # Convert the word into a set of characters to remove duplicates.
    letters = set(normalized_word)
    return len(letters) == len(normalized_word)
