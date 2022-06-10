"""Python Brasil
Lista de exercícios de estrutura de repetição.
Exercício 15: A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar
a série até o n−ésimo termo."""

termo_1 = 0
termo_2 = 1
n = int(input('Quantos termos você quer mostrar? '))
contador = 3
print(f'Os {n} primeiros termos são: {termo_1} → {termo_2}', end='')
while contador <= n:
    termo_3 = termo_1 + termo_2
    print(f' → {termo_3}', end='')
    termo_1 = termo_2
    termo_2 = termo_3
    contador += 1
print(' → Fim!')
