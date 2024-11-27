"""
In mathematics, the factorial of a non-negative integer n, denoted by n!,
is the product of all positive integers less than or equal to n.
For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.

Write a function to calculate factorial for a given input. If input is below 0
or above 12 throw an exception of type ArgumentOutOfRangeException (C#) or
IllegalArgumentException (Java) or RangeException (PHP) or throw a RangeError (JavaScript)
or ValueError (Python) or return -1 (C).
"""


def factorial(n):
    """
    Calculate the factorial of a given number.

    :param n: A non-negative integer (0 <= n <= 12)
    :return: The factorial of the number.
    :raises ValueError: If n is below 0 or above 12.
    """
    if n < 0 or n > 12:
        raise ValueError("Input must be between 0 and 12 inclusive.")
    
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
