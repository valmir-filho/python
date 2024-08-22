"""
Write a function that accepts a string, and returns the same string with all even
indexed characters in each word upper cased, and all odd indexed characters in each
word lower cased. The indexing just explained is zero based, so the zero-ith index is even,
therefore that character should be upper cased and you need to start over for each word.
The passed in string will only consist of alphabetical characters and spaces(' ').
Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').
"""


def to_weird_case(words):
    def weird_case_word(word):
        return ''.join(
            [char.upper() if index % 2 == 0 else char.lower() for index, char in enumerate(word)]
        )
    
    # Split the string into words, apply weird_case_word to each, and join them back with spaces.
    return ' '.join(weird_case_word(word) for word in words.split())
