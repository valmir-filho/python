# Unidade 04: Listas.
"""Exercício de aplicação 4: Dada a lista de dados nums = [17, 33, 23, 11, 8, 15, 9], corra a lista e identifique o maior e o menor número."""

nums = [17, 33, 23, 11, 8, 15, 9]
maior = nums[0]
menor = nums[0]
for num in nums:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print('O maior número da lista é: {} e o menor número da lista é: {}'.format(maior, menor))
