# Unidade 03: Estruturas de repetição.
# Exercício de fixação 2: Crie um programa que peça ao usuário cinco números e informe qual é o menor e qual é o maior deles.

menor = 1000000
maior = -1000000
cont = 0
for i in range (5):
    num = float(input(('Digite o numero ' + str(cont + 1) + ' de 5: ')))
    cont = cont + 1
    if num < menor:
        menor = num
    if num > maior:
        maior = num
print('O menor número é: {} e o maior número é: {}'.format(menor, maior))
