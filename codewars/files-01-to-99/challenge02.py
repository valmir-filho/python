""
In this kata you will create a function that takes in a list and returns a list with the reverse order.

Examples (Input -> Output):
1) [1, 2, 3, 4]  -> [4, 3, 2, 1]
2) [9, 2, 0, 7]  -> [7, 0, 2, 9]
"""


def reverse_list(lst):
    return lst[::-1]

# Usage examples.
example1 = [1, 2, 3, 4]
result1 = reverse_list(example1)
print(result1)  # Expected output: [4, 3, 2, 1].
example2 = [9, 2, 0, 7]
result2 = reverse_list(example2)
print(result2)  # Expected output: [7, 0, 2, 9].
