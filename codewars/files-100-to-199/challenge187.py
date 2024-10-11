"""
You are provided with a skeleton of the class "Fraction", which accepts two arguments (numerator, denominator).
Your task is to make this class string representable, and addable while keeping the result in the minimum representation possible.
"""


class Fraction:

  
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.top = numerator
        self.bottom = denominator
        self.simplify()  # Simplify the fraction upon creation.

  
    # Helper function to calculate the greatest common divisor (GCD).
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

  
    # Simplifies the fraction.
    def simplify(self):
        common_divisor = self.gcd(abs(self.top), abs(self.bottom))
        self.top //= common_divisor
        self.bottom //= common_divisor

        # Ensure the denominator is always positive.
        if self.bottom < 0:
            self.top = -self.top
            self.bottom = -self.bottom

  
    # String representation of the fraction.
    def __str__(self):
        return f"{self.top}/{self.bottom}"

  
    # Equality test.
    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num

  
    # Addition of two fractions.
    def __add__(self, other):
        new_top = self.top * other.bottom + other.top * self.bottom
        new_bottom = self.bottom * other.bottom
        return Fraction(new_top, new_bottom)
