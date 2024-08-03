"""
Given a list of integers, determine whether the sum of its elements is odd or even.
Give your answer as a string matching "odd" or "even".
If the input array is empty consider it as: [0] (array with a zero).
"""


def odd_or_even(arr):
    # Handle the case where the list is empty.
    if not arr:
        arr = [0]
    
    # Calculate the sum of the elements in the list.
    total_sum = sum(arr)
    
    # Determine if the sum is odd or even and return the appropriate string.
    if total_sum % 2 == 0:
        return "even"
    else:
        return "odd"
