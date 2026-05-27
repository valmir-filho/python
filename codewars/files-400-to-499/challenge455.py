"""
The method is supposed to remove even numbers from the list and return a list that contains the odd numbers.

However, there is a bug in the method that needs to be resolved.
"""


def kata_13_december(lst):
    # Remove os números pares e retorna apenas os ímpares.
    return [x for x in lst if x % 2 != 0]
