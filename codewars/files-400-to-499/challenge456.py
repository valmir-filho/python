"""
In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice.
Your task will be to return the sum of the numbers that occur only once.

For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15. Every other number occurs twice.

More examples in the test cases.

Good luck!

If you like this Kata, please try:

- Sum of prime-indexed elements;
- Sum of integer combinations.
"""

from collections import Counter


def repeats(arr):
    counts = Counter(arr)
    return sum(num for num, count in counts.items() if count == 1)
