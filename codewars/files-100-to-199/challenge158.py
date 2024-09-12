"""
Given the string representations of two integers, return the string representation of the sum of those integers.

For example: sumStrings('1','2') // => '3'

A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

I have removed the use of BigInteger and BigDecimal in java.

Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.
"""


def sum_strings(x, y):
    # Remove leading zeros from both numbers.
    x = x.lstrip('0')
    y = y.lstrip('0')

    # If one of the strings is empty after stripping, return the other.
    if not x:
        return y if y else '0'
    if not y:
        return x if x else '0'

    # Ensure x is the longer string, swap if necessary.
    if len(y) > len(x):
        x, y = y, x

    # Prepare for addition.
    result = []
    carry = 0

    # Pad y with zeros so it's the same length as x.
    y = y.zfill(len(x))

    # Traverse the numbers from right to left.
    for i in range(len(x) - 1, -1, -1):
        digit_sum = int(x[i]) + int(y[i]) + carry
        result.append(str(digit_sum % 10))  # Append the current digit.
        carry = digit_sum // 10  # Compute the carry.

    # If there's any carry left, append it to the result.
    if carry:
        result.append(str(carry))

    # Since we constructed the result in reverse order, reverse it back.
    return ''.join(result[::-1])
