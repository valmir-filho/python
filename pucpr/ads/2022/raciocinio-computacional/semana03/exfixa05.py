# Unidade 03: Estruturas de repetição.
# Exercício de fixação 5: Crie um programa que peça dois números ao usuário. O primeiro será o numerador e o segundo,
# o expoente. A saída do programa deve ser o resultado da operação: numerador elevado ao expoente.
# Observação: não usar função interna que calcula automaticamente potência.

numerador = float(input('Informe o valor do numerador: '))
expoente = float(input('Informe o valor do expoente: '))
print('O valor da potência de numerador {:.2f} e expoente {:.2f} é: {:.2f}'.format(numerador, expoente, (numerador ** expoente)))

