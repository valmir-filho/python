"""
You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z.
Let x be any string in the first array and y be any string in the second array.

Find max(abs(length(x) − length(y)))

If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).

Bash note:
- input: 2 strings with substrings separated by comma.
- output: number as a string
"""


def mxdiflg(a1, a2):
    if not a1 or not a2:  # Check if either array is empty.
        return -1
    
    # Calculate min and max string lengths for both arrays.
    len_a1 = [len(s) for s in a1]
    len_a2 = [len(s) for s in a2]
    
    max_a1, min_a1 = max(len_a1), min(len_a1)
    max_a2, min_a2 = max(len_a2), min(len_a2)
    
    # Calculate maximum absolute difference.
    return max(abs(max_a1 - min_a2), abs(max_a2 - min_a1))
