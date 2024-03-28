"""
I'm new to coding and now I want to get the sum of two arrays.
Actually the sum of all their elements. I'll appreciate for your help.

P.S. Each array includes only integer numbers. Output is a number too.
"""


def sum_of_two_arrays(array1, array2):
    # Calculate the sum of all elements in both arrays.
    total_sum = sum(array1) + sum(array2)
    return total_sum

# Usage example.
array1 = [1, 2, 3]
array2 = [4, 5, 6]

# Call the function with the two arrays.
result = sum_of_two_arrays(array1, array2)

# Print the result.
print(f"The sum of all elements in both arrays is: {result}.")
