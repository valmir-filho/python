""""Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for ímpar, desconsidere-o."""

soma = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        soma += n
print('Obs.: Os números digitados que são ímpares foram desconsiderados.')
print('A soma dos números pares digitados é: {}.'.format(soma))
