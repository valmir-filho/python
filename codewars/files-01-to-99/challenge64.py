"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single
integer N. Write a method that takes the array as an argument and returns this "outlier" N.
"""


def find_outlier(integers):
    # Determine the majority (even or odd) by checking the first three elements.
    sample = integers[:3]
    even_count = sum(1 for x in sample if x % 2 == 0)
    odd_count = 3 - even_count

    # Decide the majority.
    is_even_majority = even_count > odd_count

    # Find and return the outlier.
    for num in integers:
        if is_even_majority and num % 2 != 0:
            return num
        if not is_even_majority and num % 2 == 0:
            return num
