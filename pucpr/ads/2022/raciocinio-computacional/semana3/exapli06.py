# Unidade 03: Estruturas de repetição
# Exemplo de aplicação 6: Elabore um programa que solicite ao usuário dez números e efetue a soma, exibindo o resultado.
# Contudo, se em algum momento o número digitado for 0, deve interromper o laço, mostrando a soma apenas dos valores
# informados até então.

soma = 0
for i in range(10):
    num = float(input('Digite o número ' + str(i + 1) + ': '))
    if num == 0:
        break
    soma += num
print('A soma dos números informados é: {:.2f}'.format(soma))
