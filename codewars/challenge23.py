"""
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
"""


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Usage example.
test_numbers = [0, 1, 2, 3, 4, 5]
for number in test_numbers:
    print(f"{number}: {even_or_odd(number)}")
