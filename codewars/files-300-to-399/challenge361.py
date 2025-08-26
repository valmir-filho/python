"""
An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a given series of numbers.
You are provided with consecutive elements of an Arithmetic Progression. There is however one hitch: exactly one term from the original series is
missing from the set of numbers which have been given to you. The rest of the given series is the same as the original AP. Find the missing term.

You have to write a function that receives a list, list size will always be at least 3 numbers. The missing term will never be the first or last one.

Example: find_missing([1, 3, 5, 9, 11]) == 7.

PS: This is a sample question of the facebook engineer challenge on interviewstreet. I found it quite fun to solve on paper using math, derive the algo that way. Have fun!
"""


def find_missing(sequence):
    """
    Finds the missing term in an arithmetic progression.

    Args:
        sequence: A list of consecutive numbers from an arithmetic progression
                  with exactly one term missing. The list will have at least 3
                  numbers, and the missing term is never the first or last.

    Returns:
        The value of the missing term.
    """
    
    # Calculate the common difference. We check the first two differences.
    # One of them will be the true common difference, while the other will be double it.
    d1 = sequence[1] - sequence[0]
    d2 = sequence[2] - sequence[1]
    
    # Determine the correct common difference.
    # It's the one with the smaller absolute value.
    if abs(d1) < abs(d2):
        common_difference = d1
    else:
        common_difference = d2
    
    # Iterate through the sequence to find the gap.
    for i in range(len(sequence) - 1):
        if sequence[i] + common_difference != sequence[i + 1]:
            return sequence[i] + common_difference
    
    return None # This line should not be reached based on the problem description.
