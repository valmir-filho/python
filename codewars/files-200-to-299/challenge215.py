"""
Given two integer arrays a, b, both of length >= 1,
create a program that returns true if the sum of the
squares of each element in a is strictly greater than
the sum of the cubes of each element in b.
"""


def array_madness(a, b):
    # Calculate the sum of squares for array a.
    sum_squares = sum(x ** 2 for x in a)
    # Calculate the sum of cubes for array b.
    sum_cubes = sum(x ** 3 for x in b)
    # Return True if sum_squares is greater than sum_cubes.
    return sum_squares > sum_cubes
  
