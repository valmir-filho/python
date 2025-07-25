"""
My grandfather always predicted how old people would get, and right before he passed away he revealed his secret!

In honor of my grandfather's memory we will write a function using his formula!

- Take a list of ages when each of your great-grandparent died.
- Multiply each number by itself.
- Add them all together.
- Take the square root of the result.
- Divide by two.

Example: predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86

Note: the result should be rounded down to the nearest integer.

Some random tests might fail due to a bug in the JavaScript implementation. Simply resubmit if that happens to you.
"""

import math


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    # Create a list of all the ages.
    ages = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]

    # Multiply each number by itself and add them all together.
    sum_of_squares = sum(age * age for age in ages)

    # Take the square root of the result.
    square_root = math.sqrt(sum_of_squares)

    # Divide by two and round down to the nearest integer.
    predicted_age = math.floor(square_root / 2)

    return predicted_age
