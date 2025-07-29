"""
We want to generate a function that computes the series starting from 0 and ending until the given number.
"""


def show_sequence(n):
    if n < 0:
        return f"{n}<0"
    elif n == 0:
        return "0=0"
    else:
        # Calculate the sum of the series from 0 to n.
        total_sum = sum(range(n + 1))
        # Create the string representation of the series.
        series_str = "+".join(str(i) for i in range(n + 1))
        return f"{series_str} = {total_sum}"
