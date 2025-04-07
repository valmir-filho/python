"""
Remove n exclamation marks in the sentence from left to right. n is positive integer.
"""


def remove(st, n):
    result = ""
    for char in st:
        if char == "!" and n > 0:
            n -= 1  # pula esse ponto de exclamação.
        else:
            result += char  # mantém o caractere.
    return result
