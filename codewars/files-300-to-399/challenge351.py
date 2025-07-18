"""
If　a = 1, b = 2, c = 3 ... z = 26
Then l + o + v + e = 54
and f + r + i + e + n + d + s + h + i + p = 108

So friendship is twice as strong as love :-)
Your task is to write a function which calculates the value of a word based off the sum of the alphabet positions of its characters.
The input will always be made of only lowercase letters and will never be empty.
"""


def words_to_marks(s):
    # Easy one.
    total_value = 0
    for char in s:
        # Get the ASCII value of the character, subtract the ASCII value of 'a', and add 1.
        total_value += (ord(char) - ord('a') + 1)
    return total_value
