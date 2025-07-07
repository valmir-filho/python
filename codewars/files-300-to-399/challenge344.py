"""
For any given linear sequence, calculate the function [f(x)] and return it as a string.

Assumptions for this kata are:

- The sequence argument will always contain 5 values equal to f(0) - f(4);
- The function will always be in the format "nx +/- m", "x +/- m", "nx', "x" or "m";
- If a non-linear sequence simply return "Non-linear sequence" or Nothing in Haskell.
"""


def get_function(sequence):
    # Calculate the differences between consecutive terms.
    diffs = [sequence[i] - sequence[i-1] for i in range(1, len(sequence))]

    # Check if the sequence is linear.
    if len(set(diffs)) != 1:
        return "Non-linear sequence"

    # Get the common difference (n).
    n = diffs[0]

    # Calculate 'm' using the first term (f(0)).
    m = sequence[0] - n * 0

    # Construct the function string.
    if n == 0:
        return f"f(x) = {m}"
    elif n == 1:
        if m == 0:
            return "f(x) = x"
        elif m > 0:
            return f"f(x) = x + {m}"
        else:
            return f"f(x) = x - {abs(m)}"
    else:
        if m == 0:
            return f"f(x) = {n}x"
        elif m > 0:
            return f"f(x) = {n}x + {m}"
        else:
            return f"f(x) = {n}x - {abs(m)}"
