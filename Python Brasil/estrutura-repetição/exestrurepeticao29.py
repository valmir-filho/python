"""Python Brasil
Lista de exercícios de estrutura de repetição.
Exercício 29: O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar
o cálculo de quanto cada cliente deve pagar ele desenvolveu uma tabela que contém o número de itens que o cliente
comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente
leva e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que
conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:

Lojas Quase Dois — Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50"""

print('Loja Quase Dois - Tabela de Preços.')
print('💰' * 21)
for p in range(1, 51):
    print(f'{p} produto(s) é igual a: {p*1.99}.')
print('💰' * 21)