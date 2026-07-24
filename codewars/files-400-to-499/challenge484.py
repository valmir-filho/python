"""
Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

For example:
next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017

Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that contains the same digits.
Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros

some tests will include very large numbers.
test data only employs positive integers.

The function you write for this challenge is the inverse of this kata: "Next bigger number with the same digits."
"""


def next_smaller(n):
    digits = list(str(n))

    # Procura da direita para a esquerda o primeiro ponto onde seja possível diminuir o número.
    i = len(digits) - 2

    while i >= 0 and digits[i] <= digits[i + 1]:
        i -= 1

    # Os dígitos já estão na menor ordem possível.
    if i < 0:
        return -1

    # Procura à direita o maior dígito que seja menor que digits[i].
    j = len(digits) - 1

    while digits[j] >= digits[i]:
        j -= 1

    # Evita zero à esquerda.
    if i == 0 and digits[j] == '0':
        return -1

    # Troca.
    digits[i], digits[j] = digits[j], digits[i]

    # Para obter o maior número menor possível, ordenamos o restante em ordem decrescente.
    digits[i + 1:] = sorted(digits[i + 1:], reverse=True)

    return int(''.join(digits))
