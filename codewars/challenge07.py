"""
Write a function that checks if a given string (case insensitive) is a palindrome. A palindrome is a word, number, phrase, or other
sequence of symbols that reads the same backwards as forwards, such as madam or racecar.
"""


def is_palindrome(s):
    # Convert the string to lowercase.
    s = s.lower()
    # Remove non-alphanumeric characters from the string.
    s = ''.join(char for char in s if char.isalnum())
    # Check if the string is equal to its reverse.
    return s == s[::-1]

# Test the function.
print(is_palindrome("Madam"))  # Output: True
print(is_palindrome("Racecar"))  # Output: True
print(is_palindrome("Hello"))  # Output: False
