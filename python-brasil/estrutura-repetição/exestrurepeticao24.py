"""Python Brasil
Lista de exercícios de estrutura de repetição.
Exercício 24: Faça um programa que calcule o mostre a média aritmética de N notas."""

notas = []
contador = 0
while True:
    nota = float(input('Digite a nota: '))
    continuar = str(input('Deseja cadastrar mais uma nota? (S=sim/N=não): ')).strip().upper()
    notas.append(nota)
    contador += 1
    if continuar == 'N':
        print(f'A média aritmética das notas digitadas é igual a: {(sum(notas)/contador):.2f}')
        break
