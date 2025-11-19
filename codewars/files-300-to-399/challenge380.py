"""
Consider the word "abode". We can see that the letter a is in position 1 and b is in position 2.
In the alphabet, a and b are also in positions 1 and 2. Notice also that d and e in abode occupy
the positions they would occupy in the alphabet, which are positions 4 and 5.

Given an array of words, return an array of the number of letters that occupy their positions in the alphabet for each word.
"""


def solve(strings: list[str]) -> list[int]:
    result = []
    for word in strings:
        count = 0
        for i, ch in enumerate(word.lower(), start=1):
            if ord(ch) - 96 == i:
                count += 1
        result.append(count)
    return result
