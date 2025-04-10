"""
Four-digit palindromes start with [1001,1111,1221,1331,1441,1551,1551,...] and the number at position 2 is 1111.

You will be given two numbers a and b. Your task is to return the a-digit palindrome at position b if the palindromes were arranged in increasing order.

Therefore, palin(4,2) = 1111, because that is the second element of the 4-digit palindrome series.

If you like palindrome Katas, please try: Palindrome integer composition.

Life without primes.
"""


def palin(a, b):
    if a == 1:
        # 1-digit palindromes: 1 to 9.
        return b if b <= 9 else None
    half_length = (a + 1) // 2  # metade que será espelhada.
    start = 10 ** (half_length - 1)
    num = start + b - 1
    first_half = str(num)
    if a % 2 == 0:
        # Ex: 123 -> 123321.
        full_palindrome = first_half + first_half[::-1]
    else:
        # Ex: 123 -> 12321.
        full_palindrome = first_half + first_half[-2::-1]
    return int(full_palindrome)
