"""
Define a function that takes in two non-negative integers a and b and returns the last
decimal digit of a^b.

Note that a and b may be very large!

For example, the last decimal digit of 9^7 is 9, since 9^7 = 4782969.
The last decimal digit of (2^200)2^300, which has over 10^92
decimal digits, is 6. Also, please take 0^0 to be 1

You may assume that the input will always be valid.
"""


def last_digit(a, b):
    if b == 0:
        return 1  # Any number to the power of 0 is 1.

    # The last digit of a^b follows a repeating cycle of length <= 4.
    last_digit_a = a % 10
    cycle = [last_digit_a]

    # Generate the cycle of last digits.
    while True:
        next_digit = (cycle[-1] * last_digit_a) % 10
        if next_digit == cycle[0]:  # Cycle repeats.
            break
        cycle.append(next_digit)

    # Find the correct last digit using modulo.
    index = (b - 1) % len(cycle)  # -1 because list is 0-indexed.
    return cycle[index]
