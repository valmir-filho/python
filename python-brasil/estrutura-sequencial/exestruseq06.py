# Python Brasil
# Lista de exercícios de estrutura sequencial
# Exercício 6: Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

x = float(input("Informe o valor do raio do círculo: "))
y = (math.pi*(x**2))
print("O valor da área do círculo de raio",x,"é:","%.2f"%y)