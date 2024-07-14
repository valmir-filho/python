"""
You will be given a list of strings.
You must sort it alphabetically (case-sensitive,
and based on the ASCII values of the chars) and then
return the first value.
The returned value must be a string, and have "***" between
each of its letters.
You should not remove or add elements from/to the array.
"""


def two_sort(array):
    # Sort the array alphabetically.
    sorted_array = sorted(array)
    
    # Get the first string from the sorted array.
    first_string = sorted_array[0]
    
    # Join the characters of the first string with "***" in between.
    result = '***'.join(first_string)
    
    return result
