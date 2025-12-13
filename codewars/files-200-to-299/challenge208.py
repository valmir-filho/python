""
Replace all vowel to exclamation mark in the sentence.
"""


def replace_exclamation(st):
    vowels = "aeiouAEIOU"
    return ''.join('!' if char in vowels else char for char in st)
