"""
Complete the function that:

- accepts two integer arrays of equal length;
- compares the value each member in one array to the corresponding member in the other;
- squares the absolute value difference between those two values;
- returns the average of those squared absolute value difference between each member pair.
"""


def solution(array_a, array_b):
    return sum((a - b) ** 2 for a, b in zip(array_a, array_b)) / len(array_a)
