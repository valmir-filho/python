# Faça um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um número inteiro qualquer: '))
print('O dobro de {} é: {} \nO triplo é: {} \nA raiz quadrada é: {:.2f}'.format(num, (num*2), (num*3), (num**(1/2))))
