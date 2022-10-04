"""Python Brasil
Lista de exercícios de estrutura de repetição.
Exercício 4: Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de
3% e que a população de B, seja 200.000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas
as taxas de crescimento."""

pop_A = 80000
pop_B = 200000
ano = 1
while pop_A < pop_B:
    pop_A = pop_A + (pop_A * 0.03)
    pop_B = pop_B + (pop_B * 0.015)
    ano += 1
print(f'Serão necessários {ano} anos para que a população A com {pop_A:.0f} habitantes,\nultrapasse a população B'
      f'com {pop_B:.0f} habitantes.')
