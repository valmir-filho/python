"""
Comportamento singleton em modularizações no Python.

Em Python, o sistema de importação garante que um módulo seja importado apenas uma vez durante a execução de um programa. Isso significa que, mesmo se você importar o mesmo módulo de diferentes partes do seu código, Python garantirá que ele seja executado apenas uma vez e a mesma instância desse módulo será compartilhada em todos os lugares onde ele é importado.
"""

import aula89modulo

print(aula89modulo.saudacao)

for i in range(10):
    print(i)
    import aula89modulo
