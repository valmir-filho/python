"""Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final mostre:
a) Quantas vezes apareceu o número 9;
b) Em que posição foi digitado o primeiro valor 3;
c) Quais foram os números pares."""

n = int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),\
    int(input('Digite um número: '))
print(f'Os números digitados foram: {n}')
print(f'O número 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O número 3 apareceu na {n.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado nenhuma vez.')
print('Os números pares digitados foram: ', end='')
for n in n:
    if n % 2 == 0:
        print(n, end=' ')
