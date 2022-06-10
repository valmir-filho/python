"""Python Brasil
Lista de exercícios de listas.
Exercício 8: Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo
vetor. Imprima a idade e a altura na ordem inversa a ordem lida."""

idades = []
alturas = []
for c in range(1, 6):
    idade = int(input(f'Digite a idade da pessoa {c}: '))
    idades.append(idade)
    altura = float(input(f'Digite a altura da pessoa {c}: '))
    alturas.append(altura)
idades.reverse()
alturas.reverse()
print(f'As idades digitadas, na ordem inversa, são: {idades}')
print(f'As alturas digitadas, na ordem inversa, são: {alturas}')
