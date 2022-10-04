# Unidade 03: Estruturas de repetição.
# Exercício de fixação 3: Crie um programa que receba um texto digitado pelo usuário e o imprima apenas com consoantes,
# removendo as vogais. Observação: desconsiderar letras maiúsculas e acentos.

consoantes = ""
frase = str(input('Digite um texto qualquer: '))
for letra in frase:
    if letra.lower() not in "aeiou":
        consoantes = consoantes + letra
print('O texto sem as vogais fica: {}'.format(consoantes))

