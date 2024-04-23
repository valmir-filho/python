"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor "999", que é a condição de parada. No final, mostre quanto números foram digitados e qual foi a soma entre eles,
desconsiderando a flag."""

soma = contador = 0
while True:
    n = int(input('Digite um número inteiro qualquer. Digite [999] para sair: '))
    if n == 999:
        break
    soma += n
    contador += 1
print(f'Você digitou {contador} números. A soma entre eles é: {soma}.')
