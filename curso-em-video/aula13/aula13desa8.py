"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços."""

frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavras = frase.split()  # Separou as strings.
junto = ''.join(palavras)  # Juntou as strings.
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')
print()
# Outra forma de fazer esse programa sem usar o "for".
frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavras = frase.split()  # Separou as strings.
junto = ''.join(palavras)  # Juntou as strings.
inverso = junto[::-1]  # Fatiamento de strings.
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')
