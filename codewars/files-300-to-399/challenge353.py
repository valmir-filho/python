"""
Find the number with the most digits.
If two numbers in the argument array have the same number of digits,
return the first one in the array.
"""


def find_longest(arr):
    """
    Finds the number with the most digits in an array.
    If two numbers have the same number of digits, returns the first one encountered.

    Args:
        arr: A list of numbers (integers or floats).

    Returns:
        The number from the array with the most digits.
    """
    if not arr:
        return None  # Handle empty array case.

    longest_num = arr[0]
    max_digits = len(str(arr[0]).replace('.', '')) # Account for floats by removing decimal point.

    for num in arr[1:]:
        current_digits = len(str(num).replace('.', ''))
        if current_digits > max_digits:
            max_digits = current_digits
            longest_num = num
    return longest_num
