# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

# O operador "in" está procurando a palavra Silva dentro do nome digitado.
nome = str(input('Digite o seu nome completo: ')).strip()
print('O seu nome tem "SILVA"? {}'.format('SILVA' in nome.upper()))
