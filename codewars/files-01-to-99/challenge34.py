"""
The maximum sum subarray problem consists in finding the maximum sum of a contiguous
subsequence in an array or list of integers: max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])

Easy case is when the list is made up of only positive numbers and the maximum sum is the
sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is
also a valid sublist/subarray.
"""


def max_sequence(arr):
    # If the array is empty, return 0.
    if not arr:
        return 0
    
    max_current = max_global = 0
    for num in arr:
        # Calculate the maximum sum ending at the current position.
        max_current = max(num, max_current + num)
        # Update the maximum global sum found so far if the current sum is greater.
        if max_current > max_global:
            max_global = max_current
    
    # If all numbers are negative, max_global will remain 0, satisfying the problem condition.
    return max_global
