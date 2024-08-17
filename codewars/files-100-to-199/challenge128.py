"""
Write a function to split a string and convert it into an array of words.
"""


def string_to_array(input_string):
    # Check if the input string is empty.
    if input_string == "":
        return ['']
    # Otherwise, split the string into words.
    words = input_string.split()
    return words
