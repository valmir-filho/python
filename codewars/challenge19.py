"""
Make a function that returns the value multiplied by 50 and increased by 6.
If the value entered is a string it should return "Error".
"""


def multiply_and_increase(value):
    if isinstance(value, (int, float)):
        return value * 50 + 6
    else:
        return "Error"

# Examples
print(multiply_and_increase(10))  # Should return 506
print(multiply_and_increase("test"))  # Should return "Error"
