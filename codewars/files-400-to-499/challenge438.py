"""
We'll create a function that takes in two parameters:

- A sequence (length and types of items are irrelevant)
- A function (value, index) that will be called on members of the sequence and their index. The function will return either true or false.

Your function will iterate through the members of the sequence in order until the provided function returns true; at which point your function will return that item's index.

If the function given returns false for all members of the sequence, your function should return -1.

- true_if_even = lambda value, index: value % 2 == 0
- find_in_array([1,3,5,6,7], true_if_even) # --> 3
"""


def find_in_array(seq, predicate):
    for index, value in enumerate(seq):
        if predicate(value, index):
            return index
    return -1
