"""Faça um programa que tenha uma função chamada área, que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno."""


def area(l, c):
    a = l * c
    print(f'A área do terreno {l}x{c} é igual a: {a:.2f} m2.')


area(l=float(input('Digite a largura (em metros) do terreno: ')),
     c=float(input('Digite o comprimento (em metros) do terreno: ')))
