"""
Your boss decided to save money by purchasing some cut-rate optical character recognition software for scanning in the text of old novels to your database.
At first it seems to capture words okay, but you quickly notice that it throws in a lot of numbers at random places in the text.
Your harried co-workers are looking to you for a solution to take this garbled text and remove all of the numbers.
Your program will take in a string and clean out all numeric characters, and return a string with spacing and special characters ~#$%^&!@*():;"'.,? all intact.
"""


def string_clean(s):
    cleaned_string = ""
    for char in s:
        if not char.isdigit():
            cleaned_string += char
    return cleaned_string
