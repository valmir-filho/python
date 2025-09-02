"""
Write a function that given an integer n >= 0, returns an array of n ascending length subarrays, all filled with 1s.

0 => [ ]
1 => [ [1] ]
2 => [ [1], [1, 1] ]
3 => [ [1], [1, 1], [1, 1, 1] ]
"""


def pyramid(n):
    """
    Returns an array of n ascending length subarrays, all filled with 1s.
    
    Args:
        n (int): The number of subarrays. Must be a non-negative integer.
        
    Returns:
        list: A list of lists, where the i-th inner list has i+1 ones.
    """
    if n < 0:
        return []
    
    result = []
    for i in range(1, n + 1):
        result.append([1] * i)
    return result
