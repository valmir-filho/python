"""
A number is called Automorphic number if and only if its square ends in the same digits as the number itself.
For example, 25 is an automorphic number because its square (625) ends with 25.

Task: Given a positive number, determine if it is Automorphic or not. If it is, return "Automorphic", otherwise return "Not!!"
"""


def automorphic(n):
    square = n ** 2
    if str(square).endswith(str(n)):
        return "Automorphic"
    return "Not!!"
