"""
There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.
A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".
As a simplification, you may assume that no letter occurs more than once in the secret string.
You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string.
In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.
"""

from collections import defaultdict, deque


def recover_secret(triplets):
    # Criar o grafo e o contador de graus de entrada.
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    
    # Construir o grafo a partir dos triplets.
    for triplet in triplets:
        for i in range(3):
            if triplet[i] not in in_degree:
                in_degree[triplet[i]] = 0
        for i in range(2):
            a, b = triplet[i], triplet[i+1]
            if b not in graph[a]:
                graph[a].add(b)
                in_degree[b] += 1
    
    # Inicializar a fila com os nós sem pré-requisitos (grau de entrada 0).
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    result = []
    
    # Ordenação topológica.
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Verificação final.
    if len(result) == len(in_degree):
        return ''.join(result)
    else:
        raise ValueError("Ciclo detectado ou triplets insuficientes para reconstruir a string.")
