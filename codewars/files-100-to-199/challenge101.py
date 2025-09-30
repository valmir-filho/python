"""
Usually when you buy something, you're asked whether your credit card number,
phone number or answer to your most secret question is still correct.
However, since someone could look over your shoulder, you don't want that shown
on your screen. Instead, we mask it.
Your task is to write a function maskify, which changes all but the last four characters into '#'.
"""


def maskify(cc):
    # Check if the length of the string is less than or equal to 4.
    if len(cc) <= 4:
        return cc
    # Mask all but the last four characters.
    return '#' * (len(cc) - 4) + cc[-4:]
