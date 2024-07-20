"""
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
"""


def RemoveExclamationMarks(s):
    # Remove all exclamation marks from the input string and return the result.
    return s.replace('!', '')

# Usage example.
example_string = "Hello! World!! This is an example!!!"
result = RemoveExclamationMarks(example_string)
print(result)  # Output: Hello World This is an example.
