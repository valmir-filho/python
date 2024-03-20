"""
Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be builtwith the sides
of given length and false in any other case. (In this case, all triangles must have surface greater than 0 to be accepted).

Examples Input -> Output:
1) 1,2,2 -> true
2) 4,2,3 -> true
3) 2,2,2 -> true
4) 1,2,3 -> false
5) -5,1,3 -> false
6) 0,2,3 -> false
7) 1,2,9 -> false
"""


def can_form_triangle(a, b, c):
    # First, ensure all sides are of positive length.
    if a <= 0 or b <= 0 or c <= 0:
        return False
    # Check the Triangle Inequality Theorem.
    return a + b > c and a + c > b and b + c > a

# Usage examples.
print(can_form_triangle(1, 2, 2))  # Expected: True.
print(can_form_triangle(4, 2, 3))  # Expected: True.
print(can_form_triangle(2, 2, 2))  # Expected: True.
print(can_form_triangle(1, 2, 3))  # Expected: False.
print(can_form_triangle(-5, 1, 3))  # Expected: False.
print(can_form_triangle(0, 2, 3))  # Expected: False.
print(can_form_triangle(1, 2, 9))  # Expected: False.
