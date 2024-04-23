# Unidade 02: Estruturas condicionais
# Exercício de fixação 4: Crie um programa que solicite ao usuário o seu salário. Se o valor for inferior a R$ 5.000,
# calcule um abono de fim de ano de 15%. Caso contrário, o abono será de 10%.
# Informe ao usuário seu valor de abono de fim de ano.

salario = float(input("Informe o seu salário mensal (sem o indicador de milhar): "))
if salario < 5000:
    print("O seu abono de fim de ano será:", salario*0.15)
else:
    print("O seu abono de fim de ano será:", salario * 0.1)
