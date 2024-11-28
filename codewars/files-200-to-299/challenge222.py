"""
Find Mean: Find the mean (average) of a list of numbers in an array.

Information: To find the mean (average) of a set of numbers add all of the numbers together and divide by the number of values in the list.

For an example: list of 1, 3, 5, 7.

1. Add all of the numbers: 1+3+5+7 = 16.

2. Divide by the number of values in the list. In this example there are 4 numbers in the list (16/4 = 4).

3. The mean (or average) of this list is 4.
"""


def find_average(nums):
    if not nums:  # Check if the list is empty.
        return 0
    return sum(nums) / len(nums)
