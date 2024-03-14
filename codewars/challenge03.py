"""
In this kata, you are asked to square every digit of a number and concatenate them.

Examples:

1) If we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1 (81-1-1-81).
2) An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25 (49-36-25).

Note: The function accepts an integer and returns an integer.
"""


def square_digits(num):
  # Converts the number to a list of digits.
  digits = [int(digit) for digit in str(num)]
    
  # Calculate the square of each digit and concatenate the results.
  squared_digits = ''.join(str(digit ** 2) for digit in digits)
    
  # Convert the resulting string back to an integer.
  result = int(squared_digits)
    
  return result

# Usage examples.
print(square_digits(9119))  # Output: 811181.
print(square_digits(765))   # Output: 493625.
