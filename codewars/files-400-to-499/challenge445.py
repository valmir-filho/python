"""
Everyone knows passphrases. One can choose passphrases from poems, songs, movies names and
so on but frequently they can be guessed due to common cultural references.

You can get your passphrases stronger by different means. One is the following: choose a text in capital letters including or not digits and non alphabetic characters,

1. shift each letter by a given number but the transformed letter must be a letter (circular shift),
2. replace each digit by its complement to 9,
3. keep such as non alphabetic and non digit characters,
4. downcase each letter in odd position, upcase each letter in even position (the first character is in position 0),
5. reverse the whole result.

Example:

your text: "BORN IN 2015!", shift 1

1 + 2 + 3 -> "CPSO JO 7984!"

4 "CpSo jO 7984!"

5 "!4897 Oj oSpC"

With longer passphrases it's better to have a small and easy program. Would you write it?

https://en.wikipedia.org/wiki/Passphrase
"""


def play_pass(s, n):
    result = []

    for i, char in enumerate(s):
        if char.isalpha():
            # desloca a letra circularmente no alfabeto.
            shifted = chr((ord(char) - ord('A') + n) % 26 + ord('A'))

            # posição par = maiúscula, posição ímpar = minúscula.
            if i % 2 == 0:
                result.append(shifted.upper())
            else:
                result.append(shifted.lower())

        elif char.isdigit():
            # complemento para 9.
            result.append(str(9 - int(char)))

        else:
            # mantém caracteres especiais.
            result.append(char)

    return ''.join(result)[::-1]
