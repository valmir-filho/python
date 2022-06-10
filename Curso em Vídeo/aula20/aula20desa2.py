"""Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável."""


def escreva(texto):
    print('∞' * len(texto))
    print(texto)
    print('∞' * len(texto))


escreva(str(input('Digite um texto qualquer: ')).strip().upper())
