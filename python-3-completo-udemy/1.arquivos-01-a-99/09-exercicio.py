"""
Calcule o IMC e imprima o resultado da seguinte forma:

Nome Completo: Xxxxxx Xxxx  
Altura: X.XX metros
Peso: XX Kg
IMC: XX.XX
"""

nome_completo = "Valmir Moro"
altura = 1.70
peso = 70
imc = peso / (altura * altura)
# imc = peso / altura ** 2

print("Nome Completo:", nome_completo)
print("Altura:", altura)
print("Peso:", peso)
print("IMC:", imc)
