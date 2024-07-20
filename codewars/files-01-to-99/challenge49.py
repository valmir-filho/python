"""
Given a string indicating a range of letters, return a string
which includes all the letters in that range, including the last letter.
Note that if the range is given in capital letters, return the string in capitals also!
"""


def expand_range(letters_range):
    start, end = letters_range.split('-')
    if start.isupper():
        return ''.join(chr(i) for i in range(ord(start), ord(end)+1)).upper()
    else:
        return ''.join(chr(i) for i in range(ord(start), ord(end)+1)).lower()
