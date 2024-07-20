"""
Create a function taking a positive integer between 1 and 3999 (both included)
as its parameter and returning a string containing the Roman Numeral representation of that integer.
Modern Roman numerals are written by expressing each digit separately starting with the leftmost digit
and skipping any digit with a value of zero. There cannot be more than 3 identical symbols in a row.
"""


def solution(n):
    # Define the Roman numeral mappings.
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
    roman_num = ''
    i = 0
    
    while n > 0:
        for _ in range(n // val[i]):
            roman_num += syb[i]
            n -= val[i]
        i += 1
    
    return roman_num
