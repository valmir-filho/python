"""
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

- solution("abc", "bc")  # returns True
- solution("abc", "d")  # returns False
"""

def solution(text, ending):
    return text.endswith(ending)
