"""
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).
The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.
Mind the input validation.
"""


def sum_array(arr):
    if arr is None or len(arr) < 3:
        return 0

    # Remove the highest and lowest values.
    arr = sorted(arr)
    return sum(arr[1:-1])
