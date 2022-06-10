"""Crie um programa que leia vários números inteiros pelo teclado. O programa vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles,
desconsiderando a flag."""

n = contador = soma = 0
n = int(input('Digite um número inteiro qualquer (para finalizar, digite 999): '))
while n != 999:
    soma += n
    contador += 1
    n = int(input('Digite um número inteiro qualquer (para finalizar, digite 999): '))
print('Foram digitados {} números.'.format(contador))
print('A soma dos números digitados é igual a: {}.'.format(soma))
