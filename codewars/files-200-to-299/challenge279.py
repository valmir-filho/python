"""
Extend the String object (JS) or create a function (Python, C#) that converts
the value of the String to and from Base64 using the ASCII (UTF-8 for C#) character set.
"""

import base64


def to_base_64(string):
    # Codifica para bytes, aplica Base64 e remove os '=' do final.
    return base64.b64encode(string.encode('ascii')).decode('ascii').rstrip('=')

def from_base_64(string):
    # Calcula quantos '=' precisamos adicionar para o Base64 ser válido.
    padding = '=' * ((4 - len(string) % 4) % 4)
    return base64.b64decode(string + padding).decode('ascii')
