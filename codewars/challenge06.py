"""
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after
the addition. The binary number returned should be a string.

Examples: (Input1, Input2 --> Output (explanation)))

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
"""


def add_binary(a, b):
    # Adds the two numbers.
    sum = a + b
  
    # Converts the sum to binary and returns the string representation, removing the first two characters '0b' from the binary representation.
    return bin(sum)[2:]

# Testing the function with the provided examples.
test_cases = [(1, 1), (5, 9)]
test_results = [add_binary(a, b) for a, b in test_cases]
