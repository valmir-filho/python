"""Python Brasil
Lista de exercícios de estrutura de repetição.
Exercício 10: Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo
compreendido por eles."""

while True:
    n1 = int(input('Digite um número inteiro qualquer: '))
    n2 = int(input('Digite um outro número inteiro qualquer: '))
    if n1 == n2:
        print('Valores inválidos! Os números precisam ser diferentes.')
    else:
        if n1 < n2:
            print(f'Os números inteiros entre o {n1} e o {n2} são: ', end='')
            for c in range(n1, n2-1):
                print(f'{c+1}', end='-')
            print('Fim!', end='')
            break
        elif n1 > n2:
            print(f'Os números inteiros entre o {n1} e o {n2} são: ', end='')
            for c in range(n1, n2+1, -1):
                print(f'{c-1}', end='-')
            print('Fim!', end='')
            break
