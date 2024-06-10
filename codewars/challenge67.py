"""
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.
"""


def find_missing_letter(chars):
    start = ord(chars[0])
    
    for i in range(len(chars)):
        if ord(chars[i]) != start + i:
            return chr(start + i)

    return None
