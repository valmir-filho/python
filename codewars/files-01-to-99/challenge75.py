"""
In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"""


def alphabet_position(text):
    positions = []
    for char in text:
        if char.isalpha():  # Check if the character is a letter.
            position = ord(char.lower()) - ord('a') + 1  # Convert letter to its alphabet position.
            positions.append(str(position))
    return ' '.join(positions)
