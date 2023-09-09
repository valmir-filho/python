# Interpolação básica de strings.

"""
Características:
%s = string
$d e %i = int
%f = float
%x e %X = hexadecimal minúsculo e maiúsculo respectivamente (ABCDEF0123456789)
"""

nome = "Valmir"
preco = 1234.56
frase = "%s, o preço é R$%d" % (nome, preco)
# frase = "%s, o preço é R$%.2f" % (nome, preco)
print(frase)
