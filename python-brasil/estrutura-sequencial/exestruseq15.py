"""Python Brasil
Lista de exercícios de estrutura sequencial.
Exercício 15: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a) salário bruto.
b) quanto pagou ao INSS.
c) quanto pagou ao sindicato.
d) o salário líquido.
e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto: R$
- IR (11%): R$
- INSS (8%): R$
- Sindicato (5%): R$
= Salário Liquido: R$"""

import time
valor_hora = float(input('\33[32mInforme quanto você ganha por hora R$\33[m'))
quantidade_hora = float(input('\33[32mInforme quanto você trabalhou no referido mês (em hora): \33[m'))
salario_bruto = valor_hora * quantidade_hora
imposto_renda = salario_bruto * 0.11
previdencia = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = imposto_renda + previdencia + sindicato
salario_liquido = salario_bruto - descontos
print('Gerando a sua folha salarial...')
time.sleep(3)
print('\33[34mSalário Bruto: R${:.2f}'.format(salario_bruto))
print('Desconto IR(11%): R${:.2f}'.format(imposto_renda))
print('Desconto INSS(8%): R${:.2f}'.format(previdencia))
print('Desconto Sindicato(5%): R${:.2f}'.format(sindicato))
print('Salário Líquido: R${:.2f}\33[m'.format(salario_liquido))
