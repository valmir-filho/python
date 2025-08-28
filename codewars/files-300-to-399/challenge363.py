"""
In this simple exercise, you will write a function that takes two integers; n and limit; and returns a list of the multiples of n up to and possibly including limit.

It is guaranteed that n > 0 and limit >= n.

For example, if the parameters passed are (2, 6), the function should return [2, 4, 6] as 2, 4, and 6 are the multiples of 2 up to 6.
"""


def find_multiples(integer, limit):
    multiples = []
    for i in range(integer, limit + 1, integer):
        multiples.append(i)
    return multiples
