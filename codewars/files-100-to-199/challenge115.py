"""
Complete the function which takes two arguments and returns
all numbers which are divisible by the given divisor.
First argument is an array of numbers and the second is the divisor.
"""


def divisible_by(numbers, divisor):
    return [number for number in numbers if number % divisor == 0]
