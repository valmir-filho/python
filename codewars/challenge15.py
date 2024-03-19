"""
You are given two interior angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested.
"""


def find_third_angle(angle1, angle2):
    return 180 - angle1 - angle2

# Example usage
example_angle1 = 45
example_angle2 = 90
find_third_angle(example_angle1, example_angle2)
