"""
You need to write a function that reverses the words in a given string.
Words are always separated by a single space.
As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
"""


def reverse(st):
    # Split the string into words by spaces.
    words = st.split()
    # Reverse the list of words.
    reversed_words = words[::-1]
    # Join the reversed words into a single string with spaces in between.
    reversed_string = ' '.join(reversed_words)
    return reversed_string
