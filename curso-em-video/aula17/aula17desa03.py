"""Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta
(sem usar o comando "sort()"). No final, mostre a lista ordenada na tela."""

numeros = []
for n in range(0, 5):
    numero = int(input('Digite um número: '))
    if n == 0 or numero > numeros[-1]:
        numeros.append(numero)
    else:
        pos = 0
        while pos < len(numeros):
            if numero <= numeros[pos]:
                numeros.insert(pos, numero)
                break
            pos += 1
print(f'Os valores digitados foram: {numeros}')
