"""Crie um programa que leia vários números e coloque-os numa lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados respectivamente. Ao final, mostre o conteúdo das 3 listas
geradas."""

numeros = []
numeros_pares = []
numeros_impares = []
while True:
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
    continuar = str(input('Deseja continuar digitando números? (S=sim/N=não): ')).strip().upper()
    if continuar == 'N':
        break
print(f'A lista completa de números é: {numeros}')
print(f'A lista de números pares é: {numeros_pares}')
print(f'A lista de números ímpares é: {numeros_impares}')
