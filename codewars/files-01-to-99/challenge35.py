"""
Write a function that takes in a string and replaces all the vowels [a,e,i,o,u]
with their respective positions within that string.
"""


def vowel_2_index(s):
    vowels = 'aeiouAEIOU'  # Include both lowercase and uppercase vowels.
    result = []
    for index, char in enumerate(s, start=1):  # Start indexing from 1.
        if char in vowels:
            result.append(str(index))  # Append the index if the character is a vowel.
        else:
            result.append(char)  # Append the character itself if it's not a vowel.
    return ''.join(result)  # Join the list into a string.
