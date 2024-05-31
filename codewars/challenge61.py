"""
You need to design a recursive function called replicate which will receive arguments times and number.
The function should return an array containing repetitions of the number argument. For instance,
replicate(3, 5) should return [5,5,5]. If the times argument is negative, return an empty array.
As tempting as it may seem, do not use loops to solve this problem.
"""


def replicate(times, number):
    # Base case: if times is 0 or negative, return an empty list.
    if times <= 0:
        return []
    # Recursive case: append number to the result of replicate(times - 1, number).
    else:
        return [number] + replicate(times - 1, number)
