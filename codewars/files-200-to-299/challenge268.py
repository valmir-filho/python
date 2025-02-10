"""
Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James.
Since James doesn't know how to make this happen, he needs your help.

Task
You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters.
Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.
"""


def diamond(n):
    if n % 2 == 0 or n < 0:
        return None  # Retorna None se n for par ou negativo.
    
    diamond_shape = []
    for i in range(1, n + 1, 2):  # Parte superior do diamante.
        diamond_shape.append(" " * ((n - i) // 2) + "*" * i)
    
    for i in range(n - 2, 0, -2):  # Parte inferior do diamante.
        diamond_shape.append(" " * ((n - i) // 2) + "*" * i)
    
    return "\n".join(diamond_shape) + "\n"  # Junta as linhas com quebras de linha.
