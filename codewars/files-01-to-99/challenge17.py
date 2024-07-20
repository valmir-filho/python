"""
Create a function that multiplying a given number by eight if it is an even number and by nine otherwise.
"""


def multiply_by_eight_or_nine(n):
    if n % 2 == 0:  # Check if n is even.
        return n * 8
    else:
        return n * 9

# Usage example.
test_numbers = [2, 3, 4, 5, 10]
results = [multiply_by_eight_or_nine(n) for n in test_numbers]
print(results)
