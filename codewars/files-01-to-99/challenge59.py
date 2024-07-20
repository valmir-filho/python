"""
An anagram is the result of rearranging the letters of a word to produce a new word.

Note: anagrams are case insensitive.

Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
"""


def are_anagrams(word1, word2):
    # Convert both words to lowercase to ensure case insensitivity.
    word1 = word1.lower()
    word2 = word2.lower()
    
    # Sort the characters of both words.
    sorted_word1 = ''.join(sorted(word1))
    sorted_word2 = ''.join(sorted(word2))
    
    # Compare the sorted words.
    return sorted_word1 == sorted_word2
  
