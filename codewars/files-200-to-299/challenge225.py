"""
Given a non-negative integer b, write a function which returns an integer d
such that the binary representation of b is the same as the decimal representation of d.
"""


def to_binary(n):
    # Convert the number to binary (removing the "0b" prefix) and return as an integer.
    return int(bin(n)[2:])
