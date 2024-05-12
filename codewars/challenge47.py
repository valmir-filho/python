"""
Your task is to make a function that can take any non-negative
integer as an argument and return it with its digits in descending order.
Essentially, rearrange the digits to create the highest possible number.
"""


def descending_order(num):
    digits = [int(x) for x in str(num)]
    sorted_digits = sorted(digits, reverse=True)
    result = int(''.join(map(str, sorted_digits)))
    return result
