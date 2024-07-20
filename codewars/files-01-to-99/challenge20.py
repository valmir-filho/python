"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""


def shortest_word_length(s):
    # Split the string into words.
    words = s.split()
    # Find the lengths of all words.
    lengths = [len(word) for word in words]
    # Return the length of the shortest word.
    return min(lengths)

# Usage example.
test_string = "The quick brown fox jumps over the lazy dog."
print(shortest_word_length(test_string))
