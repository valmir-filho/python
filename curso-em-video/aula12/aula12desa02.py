"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 — para binário;
2 — para octal
3 — para hexadecimal."""

num = int(input('Informe um número inteiro qualquer: '))
print('''Base de conversão:
(1) converter para BINÁRIO
(2) converter para OCTAL
(3) converter para HEXADECIMAL''')
conversao = int(input('Escolha uma das 3 opções: '))
if conversao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))  # O [2:] serve para "fatiar" o
    # resultado, mostrando apenas da 3.ª casa em diante.
elif conversao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif conversao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida! Tente novamente.')
