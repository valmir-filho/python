"""
As a part of this Kata, you need to create a function that when provided with a triplet,
returns the index of the numerical element that lies between the other two elements.
The input to the function will be an array of three distinct numbers (Haskell: a tuple).
"""


def gimme(input_array):
    # Find the middle value.
    middle_value = sorted(input_array)[1]

    # Return the index of the middle value.
    return input_array.index(middle_value)
