"""
You take your son to the forest to see the monkeys.
You know that there are a certain number there (n),
but your son is too young to just appreciate the full number,
he has to start counting them from 1.

As a good parent, you will sit and count with him.
Given the number (n), populate an array with all numbers up to and
including that number, but excluding zero.
"""


def monkey_count(n):
    return list(range(1, n + 1))
