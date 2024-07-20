"""
Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
Return your answer as a number.
"""


def sum_array_values(arr):
    return sum(int(i) for i in arr)

example_array = ["3", 6, "7", 4, "2", 8]

sum_example_array = sum_array_values(example_array)

print(sum_example_array)
