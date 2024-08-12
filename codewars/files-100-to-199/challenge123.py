"""
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits.
"""


def next_bigger(n):
    digits = list(str(n))  # Convert the number to a list of its digits.

    # Start from the second last digit and move leftwards.
    for i in range(len(digits) - 2, -1, -1):
        if digits[i] < digits[i + 1]:  # Find the first digit that is smaller than the digit next to it.
            break
    else:
        return -1  # If no such digit is found, return -1.

    # Find the smallest digit to the right of 'i' that is larger than digits[i].
    for j in range(len(digits) - 1, i, -1):
        if digits[j] > digits[i]:
            break

    # Swap the found digits.
    digits[i], digits[j] = digits[j], digits[i]

    # Reverse the digits after the position i to get the smallest possible number.
    digits = digits[:i + 1] + sorted(digits[i + 1:])
    
    return int("".join(digits))
