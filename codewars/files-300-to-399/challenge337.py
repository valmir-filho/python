"""
Given an array of integers, find the minimum sum which is obtained from summing each Two integers product.

Notes:
- Array/list will contain positives only;
- Array/list will always have even size.
"""


def min_sum(arr):
  # 1. Ordena o array em ordem crescente.
  arr.sort()
  
  total = 0
  # 2. Itera enquanto o array tiver elementos.
  while arr:
    # 3. Multiplica o primeiro (menor) pelo último (maior) e adiciona à soma total. O método .pop() remove os itens da lista.
    total += arr.pop(0) * arr.pop()
    
  return total
