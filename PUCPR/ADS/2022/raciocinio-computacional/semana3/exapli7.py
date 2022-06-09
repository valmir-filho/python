# Unidade 03: Estruturas de repetição
# Exemplo de aplicação 7: Elabore um programa que solicite ao usuário dez números e efetue a multiplicação, exibindo o
# resultado. No entanto, se em algum momento o número digitado for 0, deve pular esta iteração, para que o valor não seja zerado.

mult = 1
for i in range(10):
    num = float(input('Digite o número ' + str(i + 1) + ': '))
    if num == 0:
        continue
    mult *= num
print('O resultado da multiplicação é: {:.2f}'.format(mult))
