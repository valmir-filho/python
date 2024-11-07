"""
Given a two-dimensional array of integers, return the flattened version of the array with all the integers in the sorted (ascending) order.
"""


def flatten_and_sort(array):
    # Flatten the array using a list comprehension.
    flattened = [num for sublist in array for num in sublist]
    # Sort the flattened list.
    return sorted(flattened)
