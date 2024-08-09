"""
This question is a variation on the Arithmetic Progression kata.
The following was a question that I received during a technical
interview for an entry level software developer position.
I thought I'd post it here so that everyone could give it a go: you
are given an unsorted array containing all the integers from 0 to 100 inclusively.
However, one number is missing. Write a function to find and return this number.
What are the time and space complexities of your solution?
"""


def missing_no(nums):
    # Calculate the sum of all numbers from 0 to 100.
    total_sum = 5050
    
    # Calculate the sum of the numbers in the input array.
    array_sum = sum(nums)
    
    # The missing number is the difference between the total_sum and array_sum.
    return total_sum - array_sum
