"""
Find all integers between m and n (m and n are integers with 1 <= m <= n) such that the sum of their squared divisors is itself a square.

We will return an array of subarrays or of tuples (in C an array of Pair) or a string.

The subarrays (or tuples or Pairs) will have two elements: first the number the squared divisors of which is a square and then the sum of the squared divisors.
"""

import math


def list_squared(m, n):
    result = []
    for num in range(m, n + 1):
        # Encontrar todos os divisores de num.
        divisors = set()
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                divisors.add(i)
                divisors.add(num // i)
        # Calcular a soma dos quadrados dos divisores.
        sum_of_squares = sum(d ** 2 for d in divisors)
        # Verificar se a soma é um quadrado perfeito.
        if math.isqrt(sum_of_squares) ** 2 == sum_of_squares:
            result.append([num, sum_of_squares])
    return result
