"""
Your task is simply to count the total number of lowercase letters in a string.
"""


def lowercase_count(strng):
    count = 0
    for char in strng:
        if 'a' <= char <= 'z':  # Check if the character is a lowercase letter.
            count += 1
    return count
