"""
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9.
"""


def square_sum(numbers):
    squared_numbers = [number**2 for number in numbers]  # Calculate the squares of all numbers
    return sum(squared_numbers)  # Calculate the sum of the squared numbers
