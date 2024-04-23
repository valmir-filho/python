"""Crie um programa que leia vários números e coloque-os numa lista. Depois disso, mostre:
a) Quantos números foram digitados;
b) A lista de valores ordenadas de forma decrescente;
c) Se o valor 5 foi digitado e está ou não na lista."""

numeros = []
while True:
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    continuar = str(input('Deseja continuar? (S=sim/N=não): ')).strip().upper()
    if continuar == 'N':
        break
print(f'Você digitou {len(numeros)} números.')
numeros.sort(reverse=True)
print(f'Os números digitados em ordem decrescente são: {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
