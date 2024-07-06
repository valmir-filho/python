"""
The goal of this exercise is to convert a string to a new string
where each character in the new string is "(" if that character appears
only once in the original string, or ")" if that character appears more
than once in the original string. Ignore capitalization when determining
if a character is a duplicate.
"""


def duplicate_encode(word):
    # Convert the word to lowercase to ignore capitalization.
    word = word.lower()
    # Create a dictionary to count the occurrences of each character.
    char_count = {}
    
    # Count the occurrences of each character.
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Create the encoded string based on the character counts.
    encoded_string = ""
    for char in word:
        if char_count[char] == 1:
            encoded_string += "("
        else:
            encoded_string += ")"
    
    return encoded_string
