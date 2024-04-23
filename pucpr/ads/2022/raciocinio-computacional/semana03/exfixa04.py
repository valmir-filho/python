# Unidade 03: Estruturas de repetição.
# Exercício de fixação 4: Crie um programa que solicite um número ao usuário e exiba a tabuada dele de 1 a 10, no formato:
# Tabuada do n
# n x 1 = n
# n x 2 = 2n
# e assim por diante.

num = float(input('Digite um número qualquer para saber a sua tabuada: '))
print('Tabuada do {}'.format(num))
for i in range(11):
    mult = i * num
    print(i, 'x', num, '=', '{:.2f}'.format(mult))
