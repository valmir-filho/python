"""Escreva um programa que leia 2 números inteiros e compare-os, mostrando uma mensagem na tela:
— O primeiro valor é maior;
— O segundo valor é maior;
— Não existe valor maior, os dois são iguais."""

n1 = int(input('Informe um número inteiro qualquer: '))
n2 = int(input('Informe um outro número inteiro qualquer: '))
if n1 > n2:
    print('O primeiro número é maior')
elif n1 < n2:
    print('O segundo número é maior')
else:
    print('Não existe valor maior, os dois são iguais')
