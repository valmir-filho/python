"""Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastre-os em uma única lista que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente."""

valores = [[], []]
for v in range(1, 8):
    valor = int(input(f'Digite o {v}º valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
print(f'Os valores pares são: {sorted(valores[0])}')
print(f'OS valores ímpares são: {sorted(valores[1])}')
