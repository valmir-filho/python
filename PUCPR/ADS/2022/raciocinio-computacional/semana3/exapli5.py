# Unidade 03: Estruturas de repetição
# Exemplo de aplicação 5: Elabore um programa que calcule o fatorial de um número, exibindo a informação de como é
# feito o cálculo. Exemplo: Fatorial de 5 é igual a 5*4*3*2*1.

fatorial = 1
expressao = "(cálculo: "
num = int(input('Digite um número para o cálculo do fatorial: '))
for i in range(num, 0, -1):
    fatorial *= i
    expressao += str(i)
    if i > 1:
        expressao += " * "
print('O valor do fatorial de {} é: {} {})'.format(num, fatorial, expressao))
