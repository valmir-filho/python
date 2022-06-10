"""Python Brasil
Lista de exercícios de estrutura de repetição.
Exercício 12: Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50"""

while True:
    n = int(input('Digite um número (entre 1 e 10) para gerar a sua tabuada: '))
    if n <= 0 or n > 10:
        print('Valor inválido! Digite novamente.')
    else:
        print(f'TABUADA DO {n}.')
        for c in range(1, 11):
            print(n, '*', c, '=', n*c)
        break
