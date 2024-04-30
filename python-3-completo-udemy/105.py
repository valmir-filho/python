"""
Funções recursivas e recursividade no Python.

A recursividade é uma técnica na programação em que uma função chama a si mesma para resolver um problema. No Python, assim como em muitas outras linguagens de programação, é possível escrever funções recursivas. Uma função recursiva geralmente inclui dois elementos principais:

- Caso base: este é o ponto de parada da recursão, onde a função não chama a si mesma novamente. Ele evita que a recursão continue indefinidamente.

- Caso recursivo: esta é a parte da função onde ela chama a si mesma para resolver um subproblema. A recursão deve avançar em direção ao caso base em cada chamada.
"""


def fatorial(n):
    if n == 0:
        return 1  # Caso base: fatorial de 0 é 1
    else:
        # Caso recursivo: fatorial de "n" é "n" multiplicado pelo fatorial de (n - 1)
        return n * fatorial(n - 1)


# Exemplo de uso
resultado = fatorial(5)

print(resultado)

"""
Neste exemplo, a função "fatorial" é definida de forma recursiva. Quando "n" é igual a 0, a função retorna 1 (caso base). Caso contrário, a função chama a si mesma com o argumento "n - 1" (caso recursivo) e multiplica o resultado pelo valor de "n". Isso continua até que "n" seja igual a 0, e então a recursão para.

No entanto, é importante ter cuidado ao usar recursão, pois ela pode levar a estouro de pilha (stack overflow) se não for usada com cautela e se não houver um caso base claro e a recursão não avançar em direção a ele. Certifique-se de entender bem o problema que você está resolvendo e como a recursão se encaixa nele.
"""
