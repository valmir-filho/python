"""
You're going to provide a needy programmer a utility method that generates an infinite amount of sequential fibonacci numbers.

To do this write a 'generator' starting with 1.

A fibonacci sequence starts with two 1s. Every element afterwards is the sum of the two previous elements.

See: 1, 1, 2, 3, 5, 8, 13, ..., 89, 144, 233, 377, ...
"""


def all_fibonacci_numbers():
    a, b = 1, 1

    while True:
        yield a
        a, b = b, a + b
