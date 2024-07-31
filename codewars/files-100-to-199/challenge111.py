"""
The vowel substrings in the word codewarriors are o,e,a,io.
The longest of these has a length of 2. Given a lowercase string
that has alphabetic characters only (both vowels and consonants)
and no spaces, return the length of the longest vowel substring.
Vowels are any of aeiou.
"""


def solve(s):
    vowels = set('aeiou')
    max_length = 0
    current_length = 0

    for char in s:
        if char in vowels:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
        else:
            current_length = 0
    
    return max_length
