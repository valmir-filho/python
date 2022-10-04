"""Python Brasil
Lista de exercícios de listas.
Exercício 4: Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
Imprima as consoantes."""

consoantes = []
vogais = 'AEIOU'
contador = 0
for c in range(1, 11):
    caracter = str(input(f'Digite o caracter número {c}: ')).strip().upper()
    if caracter not in vogais:
        consoantes.append(caracter)
        contador += 1
print(f'Foram digitadas {contador} consoantes.')
print(f'As consoantes digitadas foram: {consoantes}.')
