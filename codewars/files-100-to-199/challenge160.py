"""
In this Kata we are passing a number (n) into a function.
Your code will determine if the number passed is even (or not).
The function needs to return either a true or false.
Numbers may be positive or negative, integers or floats.
Floats with decimal part non equal to zero are considered UNeven for this kata.
"""


def is_even(n):
    # Check if n is a float with a non-zero decimal part.
    if isinstance(n, float) and n % 1 != 0:
        return False
    
    # Check if n is an integer and divisible by 2.
    return n % 2 == 0
