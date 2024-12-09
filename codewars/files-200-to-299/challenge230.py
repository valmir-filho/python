"""
In Python, there is a built-in filter function that operates similarly to JS's filter.

For more information on how to use this function, visit https://docs.python.org/3/library/functions.html#filter
"""


def get_even_numbers(arr):
    return list(filter(lambda x: x % 2 == 0, arr))
