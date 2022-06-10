"""Python Brasil
Lista de exercícios de estrutura de decisão.
Exercício 12: Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
Salário Bruto: (5 * 220)        : R$1100,00
(-) IR (5%)                     : R$55,00
(-) INSS (10%)                  : R$110,00
FGTS (11%)                      : R$121,00
Total de descontos              : R$165,00
Salário Liquido                 : R$935,00"""

import time
print()
valor_hora = float(input('\33[32mInforme o valor da sua hora de trabalho: R$'))
quant_hora = float(input('Informe a quantidade de horas trabalhadas no mês: \33[m'))
salario_bruto = valor_hora * quant_hora
print()
print('Gerando a folha de pagamento...')
time.sleep(3)
print()
print('Salário Bruto ({} x {}): R${:.2f}'.format(valor_hora,quant_hora,salario_bruto))
if salario_bruto <= 900:
    print('(-) IR: Isento')
elif 900 < salario_bruto <= 1500:
    print('(-) IR (5%): R${:.2f}'.format(salario_bruto*0.05))
elif 1500 < salario_bruto <= 2500:
    print('(-) IR (10%): R${:.2f}'.format(salario_bruto * 0.1))
else:
    print('(-) IR (20%): R${:.2f}'.format(salario_bruto * 0.2))
print('(-) Sindicato (3%): R${:.2f}'.format(salario_bruto*0.03))
print('(-) INSS (10%): R${:.2f}'.format(salario_bruto*0.1))
print('FGTS (11%): R${:.2f}'.format(salario_bruto*0.11))
if salario_bruto <= 900:
    print('Total de Descontos: R${:.2f}'.format(salario_bruto*0.13))
elif 900 < salario_bruto <= 1500:
    print('Total de Descontos: R${:.2f}'.format(salario_bruto*0.18))
elif 1500 < salario_bruto <= 2500:
    print('Total de Descontos: R${:.2f}'.format(salario_bruto*0.23))
else:
    print('Total de Descontos: R${:.2f}'.format(salario_bruto*0.33))
if salario_bruto <= 900:
    print('Salário Líquido: R${:.2f}'.format(salario_bruto-salario_bruto*0.13))
elif 900 < salario_bruto <= 1500:
    print('Salário Líquido: R${:.2f}'.format(salario_bruto-salario_bruto*0.18))
elif 1500 < salario_bruto <= 2500:
    print('Salário Líquido: R${:.2f}'.format(salario_bruto-salario_bruto*0.23))
else:
    print('Salário Líquido: R${:.2f}'.format(salario_bruto-salario_bruto*0.33))
