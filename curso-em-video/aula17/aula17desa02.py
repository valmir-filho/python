"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente."""

numeros = []
while True:
    numero = float(input('Digite um número qualquer: '))
    if numero in numeros:
        print('Número duplicado! Não será adicionado.')
    else:
        numeros.append(numero)
    continuar = str(input('Deseja continuar digitando números? (S=sim/N=não): ')).strip().upper()
    if continuar == 'N':
        break
print(f'Os número digitados, em ordem crescente, foram: {sorted(numeros)}')
