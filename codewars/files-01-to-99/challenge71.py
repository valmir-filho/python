"""
Create a function that returns the sum of the two lowest positive
numbers given an array of minimum 4 positive integers.
No floats or non-positive integers will be passed.
"""


def sum_two_smallest_numbers(numbers):
    # Sort the list to find the two smallest numbers.
    sorted_numbers = sorted(numbers)
    # Return the sum of the first two elements in the sorted list.
    return sorted_numbers[0] + sorted_numbers[1]
