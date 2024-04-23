num1 = float(input('Digite um 1º número qualquer: '))
num2 = float(input('Digite um 2º número qualquer: '))
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
div_inteira = num1 // num2
rest_div = num1 % num2
potencia = num1 ** num2
print('O resultado da soma do {} com o {} é: {}'.format(num1, num2, soma))
print('O resultado da subtração do {} com o {} é: {}'.format(num1, num2, subtracao))
print('O resultado da multiplicação do {} com o {} é: {}'.format(num1, num2, multiplicacao))
print('O resultado da divisão do {} com o {} é: {:.2f}'.format(num1, num2, divisao))
print('O resultado da divisão inteira do {} com o {} é: {}'.format(num1, num2, div_inteira))
print('O resto do resultado da divisão do {} com o {} é: {:.2f}'.format(num1, num2, rest_div))
print('O resultado do {} elevado a {} é: {}'.format(num1, num2, potencia))
