"""
In this Kata, you will be given a string and two indexes (a and b).
Your task is to reverse the portion of that string between those two indices inclusive.

str = "codewars", a = 1, b = 5 --> "cawedors"
str = "cODEWArs", a = 1, b = 5 --> "cAWEDOrs"

Input will be lowercase and uppercase letters only.

The first index a will always be smaller than the string length; the second index b can be greater than the string length.

More examples in the test cases. Good luck!

Please also try:

- Simple time difference;
- Simple remove duplicates.
"""


def solve(st, a, b):
    # Ajusta b caso seja maior que o tamanho da string.
    b = min(b, len(st) - 1)
    
    # Divide a string em três partes.
    before = st[:a]
    middle = st[a:b+1][::-1]  # inverte a parte desejada.
    after = st[b+1:]
    
    return before + middle + after
