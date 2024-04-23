"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais."""

palavras = ('abacate', 'melancia', 'abacaxi', 'pera', 'melao', 'uva', 'pessego', 'kiwi', 'banana', 'morango', 'mamao')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as seguintes vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
