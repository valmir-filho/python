"""
Define a function that removes duplicates from an array of non
negative numbers and returns it as a result.
The order of the sequence has to stay the same.
"""


def distinct(seq):
    seen = set()  # To store unique elements.
    result = []  # To store the result in order.

    for num in seq:
        if num not in seen:  # Check if the number is already seen.
            seen.add(num)  # Add to seen set.
            result.append(num)  # Append to result list.
    
    return result
