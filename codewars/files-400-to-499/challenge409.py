"""
Reverse every other word in a given string, then return the string.
Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word.
Punctuation marks should be treated as if they are a part of the word in this kata.
"""


def reverse_alternate(st):
    words = st.split()
    
    for i in range(len(words)):
        if i % 2 == 1:
            words[i] = words[i][::-1]
    
    return " ".join(words)
