"""
You will be given an array and a limit value. You must check that all values in the array
are below or equal to the limit value. If they are, return true. Else, return false.

You can assume all values in the array are numbers.
"""


def check_array_against_limit(array, limit):
    # Check each value in the array.
    for value in array:
        if value > limit:
            return False
    return True

# Usage example.
array = [10, 20, 30, 40]
limit = 50
result = check_array_against_limit(array, limit)
print("All values are within the limit:", result)
