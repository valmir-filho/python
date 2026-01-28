"""
You will be given an array of numbers.
You have to sort the odd numbers in ascending
order while leaving the even numbers at their
original positions.
"""


def sort_array(source_array):
    # Extract odd numbers and sort them.
    sorted_odds = sorted([num for num in source_array if num % 2 != 0])
    
    # Use an iterator for sorted_odds to place each odd number in sorted order.
    odd_iterator = iter(sorted_odds)
    result = [
        next(odd_iterator) if num % 2 != 0 else num for num in source_array
    ]
    
    return result
