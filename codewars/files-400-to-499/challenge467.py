"""
I love Fibonacci numbers in general, but I must admit I love some more than others.

I would like for you to write me a function that, when given a number n (n >= 1 ), returns the nth number in the Fibonacci Sequence.

For example: nth_fib(4) == 2

Because 2 is the 4th number in the Fibonacci Sequence.

For reference, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two.
"""


def nth_fib(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a
