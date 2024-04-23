"""Python Brasil
Lista de exercícios de estrutura de repetição.
Exercício 5: altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
Programa anterior: supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de
crescimento de 3% e que a população de B, seja 200.000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa
que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do
país B, mantidas as taxas de crescimento."""

pop_A = pop_B = 0
ano = 0
while True:
    pop_A = int(input('Informe a população do país A: '))
    taxa_crescimento_A = float(input('Informe a taxa de crescimento (em %) da população do país A: '))
    pop_B = int(input('Informe a população do país B: '))
    taxa_crescimento_B = float(input('Informe a taxa de crescimento (em %) da população do país B: '))
    while pop_A < pop_B:
        pop_A = pop_A + (pop_A * (taxa_crescimento_A/100))
        pop_B = pop_B + (pop_B * (taxa_crescimento_B/100))
        ano += 1
    print(f'Serão necessários {ano} anos para que a população A com {pop_A:.0f} habitantes, ultrapasse a população B com {pop_B:.0f} habitantes.')
