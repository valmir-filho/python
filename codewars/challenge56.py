"""
In this Kata, you will be given an array of arrays and your task will be to
return the number of unique arrays that can be formed by picking exactly one
element from each subarray.
"""


from itertools import product

def unique_combinations(arrays):
    # Generate all combinations by picking one element from each subarray.
    all_combinations = product(*arrays)
    # Convert combinations to set to get unique combinations.
    unique_combinations = set(all_combinations)
    # Return the number of unique combinations.
    return len(unique_combinations)
