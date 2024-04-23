# Unidade 03: Estruturas de repetição
# Exemplo de aplicação 9: Elabore um programa que solicite ao usuário que digite indefinidamente números e efetue a
# soma, parando apenas quando o usuário digitar o número 0.

soma = 0
num = -1
while num != 0:
    num = float(input('Digite um número qualquer (quando quiser parar de somar, digite 0): '))
    soma += num
print('A soma dos números é: {:.2f}'.format(soma))
