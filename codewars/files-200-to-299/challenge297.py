"""
ISBN-10 identifiers are ten digits long. The first nine characters are digits 0-9. The last digit can be 0-9 or X, to indicate a value of 10.
An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero.
"""


def valid_ISBN10(isbn): 
    # Verifica se o tamanho é 10.
    if len(isbn) != 10:
        return False
    
    total = 0
    for i in range(10):
        char = isbn[i]
        # O último caractere pode ser 'X' que vale 10.
        if i == 9 and char == 'X':
            digit = 10
        elif char.isdigit():
            digit = int(char)
        else:
            return False  # caractere inválido.
        total += digit * (i + 1)
    
    return total % 11 == 0
