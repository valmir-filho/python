"""
Create the function prefill that returns an array of n elements that all have the same value v. See if you can do this without using a loop.

You have to validate input:

- v can be anything (primitive or otherwise);
- if v is ommited, fill the array with undefined;
- if n is 0, return an empty array;
- if n is anything other than an integer or integer-formatted string (e.g. '123') that is >=0, throw a TypeError.

When throwing a TypeError, the message should be n is invalid, where you replace n for the actual value passed to the function.
"""


def prefill(n, v=None):
    try:
        # Attempt to convert n to an integer.
        n = int(n)
        if n < 0:
            raise ValueError
    except (ValueError, TypeError):
        raise TypeError(f"{n} is invalid")

    # Return the array filled with v, with n elements.
    return [v] * n
