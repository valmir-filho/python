"""
Given an array of ones and zeroes, convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

Examples:
1) Testing: [0, 0, 0, 1] ==> 1.
2) Testing: [0, 0, 1, 0] ==> 2.
3) Testing: [0, 1, 0, 1] ==> 5.
4) Testing: [1, 0, 0, 1] ==> 9.
5) Testing: [0, 0, 1, 0] ==> 2.
6) Testing: [0, 1, 1, 0] ==> 6.
7) Testing: [1, 1, 1, 1] ==> 15.
8) Testing: [1, 0, 1, 1] ==> 11.

However, the arrays can have varying lengths, not just limited to 4.
"""


def binary_array_to_number(arr):
    result = 0
    for bit in arr:
        result = result * 2 + bit
    return result

# Test cases.
test_cases = [
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 0, 1, 1]
]

for test in test_cases:
    print(f"Testing: {test} ==> {binary_array_to_number(test)}")
