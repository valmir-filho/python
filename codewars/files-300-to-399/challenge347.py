"""
Write a method that will search an array of strings for all strings that contain another string, ignoring capitalization. Then return an array of the found strings.
The method takes two parameters, the query string and the array of strings to search, and returns an array.
If the string isn't contained in any of the strings in the array, the method returns an array containing a single string: "Empty" (or Nothing in Haskell, or "None" in Python and C).
"""


def word_search(query, seq):
    """
    Searches an array of strings for all strings that contain another string, ignoring capitalization.

    Args:
        query (str): The string to search for.
        seq (list): The array of strings to search within.

    Returns:
        list: An array of the found strings, or ["None"] if no strings are found.
    """
    found_strings = []
    # Convert the query to lowercase once for efficient comparison.
    query_lower = query.lower()

    for s in seq:
        # Convert each string in the sequence to lowercase for case-insensitive comparison.
        if query_lower in s.lower():
            found_strings.append(s)

    if not found_strings:
        return ["None"]
    else:
        return found_strings
  
