"""
Given two numbers and an arithmetic operator (the name of it, as a string),
return the result of the two numbers having that operator used on them.
A and B will both be positive integers, and a will always be the first
number in the operation, and b always the second.
The four operators are "add", "subtract", "divide", "multiply".
"""


def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        # Ensure to handle division by zero if needed.
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed"
    else:
        return "Error: Invalid operator"
