"""Python Brasil
Lista de exercícios de listas.
Exercício 3: Faça um Programa que leia 4 notas, mostre as notas e a média na tela."""

notas = []
contador = 0
for n in range(1, 5):
    nota = float(input(f'Digite a nota {n}: '))
    notas.append(nota)
    contador += 1
print(f'As notas digitadas foram: {notas}')
print(f'A média das notas é: {sum(notas)/contador:.2f}.')
