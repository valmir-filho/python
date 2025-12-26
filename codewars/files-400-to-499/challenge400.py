"""
Find the last element of the given argument(s). If a single argument is passed and is a list/array or a string, return its last element.
It is guaranteed that there will be at least one argument and that single-argument arrays/lists/strings will not be empty.
"""


def last(*args):
    # Se houver apenas um argumento.
    if len(args) == 1:
        value = args[0]
        # Se for lista, tupla ou string, retorna o último elemento.
        if isinstance(value, (list, tuple, str)):
            return value[-1]
        # Caso contrário, retorna o próprio valor.
        return value
    # Se houver múltiplos argumentos, retorna o último argumento.
    return args[-1]
