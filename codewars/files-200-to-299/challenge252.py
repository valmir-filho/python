"""
Your task is to remove all duplicate words from a string, leaving only single (first) words entries.
"""


def remove_duplicate_words(s):
    # Split the string into words.
    words = s.split()
    # Use an ordered set to keep track of seen words.
    seen = set()
    result = []
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    # Join the result back into a string.
    return ' '.join(result)
