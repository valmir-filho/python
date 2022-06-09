# Unidade 04: Listas.
"""Exercício de fixação 6: dado o vetor nums = [3, 7, 2, 9, 5, 6], crie um programa que, em uma linha, calcule a média
dos seus elementos."""

nums = [3, 7, 2, 9, 5, 6]
media = sum(nums) / len(nums)
print('O vetor é: {}'.format(nums))
print('A média dos números do vetor é: {:.2f}'.format(media))
