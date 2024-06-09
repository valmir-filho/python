"""
You are given an odd-length array of integers, in which all of them are the same, except for one single number.
Complete the method which accepts such an array, and returns that single different number.
The input array will always be valid! (odd-length >= 3).
"""


def stray(arr):
    counts = {}
    
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    for num, count in counts.items():
        if count == 1:
            return num
