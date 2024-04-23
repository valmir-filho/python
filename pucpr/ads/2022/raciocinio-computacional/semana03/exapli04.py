# Unidade 03: Estruturas de repetição
# Exemplo de aplicação 4: Elabore um programa que solicite três números, some-os e exiba o resultado para o usuário.

soma = 0
for i in range(3):
    num = int(input('Digite o número ' + str(i + 1) + ' : '))
    soma += num
print('A soma dos números é:', soma)
