"""
Kevin is noticing his space run out! Write a function that removes the spaces from the values and returns an array showing the space decreasing.
"""


def spacey(array):
    result = []
    current = ""
    for word in array:
        current += word  # Concatenate the word to the current string.
        result.append(current)  # Add the updated string to the result list.
    return result
