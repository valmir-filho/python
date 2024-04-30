# Formatação de strings (f-strings).

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

print(f"Nome Completo: {nome_completo}")
print(f"Altura: {altura:.2f}m")
print(f"Peso: {peso}Kg")
print(f"IMC: {imc:.2f}")
