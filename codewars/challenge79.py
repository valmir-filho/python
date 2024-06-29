"""
Write two functions that convert a roman numeral to and from an integer value.
Multiple roman numeral values will be tested for each function.
Modern Roman numerals are written by expressing each digit separately starting
with the left most digit and skipping any digit with a value of zero.
"""


class RomanNumerals:
    @staticmethod
    def to_roman(val: int) -> str:
        val_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        roman = ''
        for (num, symbol) in val_map:
            while val >= num:
                roman += symbol
                val -= num
        return roman

    @staticmethod
    def from_roman(roman_num: str) -> int:
        roman_map = {
            'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
            'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
            'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
        }
        
        i = 0
        val = 0
        while i < len(roman_num):
            if i + 1 < len(roman_num) and roman_num[i:i+2] in roman_map:
                val += roman_map[roman_num[i:i+2]]
                i += 2
            else:
                val += roman_map[roman_num[i]]
                i += 1
        return val
