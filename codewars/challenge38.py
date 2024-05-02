"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
"""


def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(i)
            array.append(i)
    return array
