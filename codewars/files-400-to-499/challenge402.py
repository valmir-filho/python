"""
Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

If the array is invalid (empty, or contains negative integers or integers with more than 1 digit), return nil (or your language's equivalent).

Examples:

Valid arrays

[4, 3, 2, 5] would return [4, 3, 2, 6] (4325 + 1 = 4326)
[1, 2, 3, 9] would return [1, 2, 4, 0] (1239 + 1 = 1240)
[9, 9, 9, 9] would return [1, 0, 0, 0, 0] (9999 + 1 = 10000)
[0, 1, 3, 7] would return [0, 1, 3, 8] (0137 + 1 = 0138)

Invalid arrays

[] is invalid because it is empty
[1, -9] is invalid because -9 is not a non-negative integer
[1, 2, 33] is invalid because 33 is not a single-digit integer
"""


def up_array(arr):
    # validações
    if not arr:
        return None
    
    for x in arr:
        if not isinstance(x, int) or x < 0 or x > 9:
            return None
    
    # soma 1 ao número representado.
    i = len(arr) - 1
    while i >= 0:
        if arr[i] < 9:
            arr[i] += 1
            return arr
        arr[i] = 0
        i -= 1
    
    # se todos eram 9.
    return [1] + arr
