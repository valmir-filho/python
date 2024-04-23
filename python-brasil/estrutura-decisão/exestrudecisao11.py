"""Python Brasil
Lista de exercícios de estrutura de decisão.
Exercício 11: as Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
desenvolver o programa que calculará os reajustes. Faça um programa que receba o salário de um colaborador e o reajuste
segundo o seguinte critério, baseado no salário atual:
salários até R$280,00 (incluindo): aumento de 20%
salários entre R$280,00 e R$700,00: aumento de 15%
salários entre R$700,00 e R$1500,00: aumento de 10%
salários de R$1500,00 em diante: aumento de 5%
Após o aumento ser realizado, informe na tela:
— o percentual de aumento aplicado;
— o valor do aumento;
— o novo salário, após o aumento."""

print()
salario = float(input('\33[32mInforme o valor do seu salário: R$\33[m'))
print()
if salario <= 280:
    print('Percentual de aumento: 20%')
    print('O seu aumento será de R${:.2f}'.format(salario*0.2))
    print('Seu salário passará a ser de R${:.2f}'.format(salario+(salario*0.2)))
elif 280 < salario <= 700:
    print('Percentual de aumento: 15%')
    print('O seu aumento será de R${:.2f}'.format(salario*0.15))
    print('Seu salário passará a ser de R${:.2f}'.format(salario+(salario*0.15)))
elif 700 < salario <= 1500:
    print('Percentual de aumento: 10%')
    print('O seu aumento será de R${:.2f}'.format(salario*0.1))
    print('Seu salário passará a ser de R${:.2f}'.format(salario+(salario*0.1)))
else:
    print('Percentual de aumento: 5%')
    print('O seu aumento será de R${:.2f}'.format(salario * 0.05))
    print('Seu salário passará a ser de R${:.2f}'.format(salario + (salario * 0.05)))
