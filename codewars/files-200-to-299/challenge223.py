"""
Create a function which accepts one arbitrary string as an argument, and return a string of length 26.

The objective is to set each of the 26 characters of the output string to either "1" or "0"
based on the fact whether the Nth letter of the alphabet is present in the input (independent of its case).

So if an "a" or an "A" appears anywhere in the input string (any number of times), set the first character
of the output string to "1", otherwise to "0". if "b" or "B" appears in the string, set the second character
to "1", and so on for the rest of the alphabet.
"""


def change(st):
    # Create a string representing all letters of the alphabet.
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Initialize the output string with '0' for each letter.
    result = ['0'] * 26
    
    # Iterate over each character in the input string, converted to lowercase.
    for char in st.lower():
        # If the character is a letter, update the corresponding position to "1".
        if char in alphabet:
            result[alphabet.index(char)] = '1'
    
    # Return the joined result as a single string.
    return ''.join(result)
