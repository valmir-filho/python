"""Crie um programa que leia vários números inteiros pelo teclado. O programa vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles,
desconsiderando a flag."""

n = 0
contador = 0
flag = 999
soma = []
while n != flag:
    n = int(input('Digite um número inteiro qualquer (para finalizar, digite 999): '))
    contador += 1
    soma.append(n)
print('Foram digitados {} números.'.format(contador - 1))
print('A soma dos números digitados é igual a: {}.'.format(sum(soma)-flag))
