# Aplicações de variáveis compostas em Python.
# Tuplas (são imutáveis e posso guardar tipos de dados diferentes dentro da mesma tupla.)

print()
lanche = ('pudim', 'pizza', 'hambúrguer', 'suco')
print(lanche)  # Imprime todas as informações da tupla chamada lanche.
print()
print(lanche[1])  # Imprime a informação da posição 1 da tupla chamada lanche. Lembrando que, nesse caso, a posição
# inicia em zero e vai da esquerda para a direita.
print()
print(lanche[-3])  # Imprime a informação da posição -3 da tupla chamada lanche. Lembrando que, nesse caso, a posição
# inicia em -1 e vai da direita para a esquerda.
print()
print(lanche[0:3])  # Imprime as informações da posição 0 até 2 da tupla chamada lanche. A última posição (3), o Python
# desconsidera.
print()
print(lanche[2:])  # Imprime as informações da posição 2 até o final da tupla chamada lanche.
print()
print(lanche[:2])  # Imprime as informações do início da tupla até a posição 1. A última posição (2), o Python
# desconsidera.
print()
for comida in lanche:  # Imprime todos os itens (contador chamado "comida" da tupla "lanche").
    print(f'Eu vou comer {comida}')
print()
for comida in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[comida]}')
print()
for posicao, comida in enumerate(lanche):  # O comando enumerate enumera os itens da tupla.
    print(f'Eu vou comer {comida} na posição {posicao}.')
print()
print(sorted(lanche))  # Imprime em ordem (alfabética ou numérica) a tupla.
print()
a = (1, 2, 3, 4)
b = (8, 7, 6, 5)
c = a+b  # Juntei duas tuplas em outra.
print(c)
print(len(c))  # Imprime o tamanho da tupla.
print(c.count(3))  # Imprime quantas vezes o número 3 está aparecendo na tupla c.
print(c.index(8))  # Imprime em que posição está o número 8 dentra da tupla.
print()
del lanche  # Deleta a tupla toda.
