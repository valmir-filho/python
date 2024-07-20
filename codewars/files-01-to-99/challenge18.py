"""
When provided with a letter, return its position in the alphabet.

Example Input -> Output:
1) a -> Position 1 of alphabet.
"""


def letter_position(letter):
    position = ord(letter.lower()) - 96
    return f"Position {position} of alphabet."

# Usage example.
input_letter = "a"
print(letter_position(input_letter))
