"""
Given an array of integers, your function bubblesortOnce/bubblesort_once/BubblesortOnce
(or equivalent, depending on your language's naming conventions) should return a new array
equivalent to performing exactly 1 complete pass on the original array. Your function should
be pure, i.e. it should not mutate the input array.
"""


def bubblesort_once(l):
    # Make a copy of the input list to avoid mutating the original list.
    new_list = l[:]
    
    # Perform a single pass of the Bubble Sort algorithm.
    for i in range(len(new_list) - 1):
        if new_list[i] > new_list[i + 1]:
            # Swap the elements
            new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
    
    return new_list
