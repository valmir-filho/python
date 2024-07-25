"""
Can you find the needle in the haystack?
Write a function findNeedle() that takes
an array full of junk but containing one "needle"
"""


def find_needle(haystack):
    # Iterate through the array to find the needle.
    for index, item in enumerate(haystack):
        if item == "needle":
            return f"found the needle at position {index}"
    # If needle is not found, return a message.
    return "needle not found"
