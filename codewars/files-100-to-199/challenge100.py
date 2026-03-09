""
Write a function that takes in a string of one or more words,
and returns the same string, but with all words that have five
or more letters reversed (Just like the name of this Kata).
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
"""


def spin_words(s):
    words = s.split()
    result = []
    
    for word in words:
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)
    
    return ' '.join(result)
