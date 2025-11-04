"""
Complete the method which returns the number which is most frequent in the given input array.
If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.
"""


def highest_rank(arr):
    return max(sorted(arr), key=lambda x: (arr.count(x), x))
