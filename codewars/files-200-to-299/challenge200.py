""
Given a 2D (nested) list (array, vector, ...) of size m * n, your task is to find the sum of the minimum values in each row.
"""


def sum_of_minimums(numbers):
    # Use a list comprehension to find the minimum of each row and sum them.
    return sum(min(row) for row in numbers)
