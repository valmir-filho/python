"""
Write a function that accepts an array of 10 integers (between 0 and 9),
that returns a string of those numbers in the form of a phone number.
"""


def create_phone_number(numbers):
    if len(numbers) != 10 or not all(0 <= num <= 9 for num in numbers):
        raise ValueError("Input must be an array of 10 integers between 0 and 9.")
    
    phone_number = "({}{}{}) {}{}{}-{}{}{}{}".format(*numbers)
    return phone_number
  
