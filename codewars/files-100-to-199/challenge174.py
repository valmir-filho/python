"""
Write a function that takes an array of unique integers and
returns the minimum number of integers needed to make the
values of the array consecutive from the lowest number to
the highest number.
"""


def consecutive(arr):
    if not arr:  # Handle empty array case.
        return 0
    
    min_val = min(arr)
    max_val = max(arr)
    
    # Calculate total numbers needed for consecutive range.
    total_needed = max_val - min_val + 1
    
    # The number of integers we already have.
    existing_numbers = len(arr)
    
    # The number of integers we need to add.
    return total_needed - existing_numbers
