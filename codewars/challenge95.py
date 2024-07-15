"""
Complete the function/method so that it takes a PascalCase string and returns
the string in snake_case notation. Lowercase characters can be numbers.
If the method gets a number as input, it should return a string.
"""

import re


def to_underscore(string):
    if isinstance(string, int):
        return str(string)
    
    # Insert underscores before uppercase letters and convert to lowercase.
    snake_case_string = re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
    
    return snake_case_string
