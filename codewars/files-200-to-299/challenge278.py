"""
Your goal is to return multiplication table for number that is always an integer from 1 to 10.
"""


def multi_table(number):
    return '\n'.join(f"{i} * {number} = {i * number}" for i in range(1, 11))
