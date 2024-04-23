"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes."""

l1 = float(input('Informe a medida do lado 1 do triângulo: '))
l2 = float(input('Informe a medida do lado 2 do triângulo: '))
l3 = float(input('Informe a medida do lado 3 do triângulo: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Esses valores formam um triângulo ', end='')  # o end='' serve para não pular para a próxima linha.
    if l1 == l2 == l3:
        print('equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('isóceles')
    elif l1 != l2 != l3 != l1:
        print('escaleno')
else:
    print('Os lados informados não formam um triângulo')
