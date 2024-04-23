""""Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 que se encontram no
intervalo de 1 até 500."""

soma = 0
valores = 0
for c in range(1, 500, 2):
    if (c % 3) == 0:
        soma += c
        valores += 1
print('A soma dos {} valores solicitados é igual a: {}.'.format(valores, soma))
