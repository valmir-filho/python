# Unidade 06: Funções
# Funções no Python
# Ela pode ser usada diversas vezes no mesmo script, alterando apenas os seus dados.

"""Questão relacionada a escopo é o tempo de vida das variáveis criadas dentro da função. Uma variável criada numa
função tem o seu tempo de vida limitado ao seu escopo. Além disso, ela tem precedência de acesso frente a uma variável
externa ao escopo, mesmo tendo o mesmo nome. Segue um exemplo:"""

def minha_funcao():
    x = 10
    print('Valor de x dentro da função: {}'.format(x))
x = 20
minha_funcao()
print('Valor de x fora da função: {}'.format(x))
print()

# Essa diferença ocorre pela precedência da variável criada com o mesmo nome dentro do escopo da função. No caso da
# remoção da linha 9, a variável pública x estaria visível dentro da função "minha_funcao()", gerando o seguinte
# resultado:

def minha_funcao():
    print('Valor de x dentro da função: {}'.format(x))
x = 20
minha_funcao()
print('Valor de x fora da função: {}'.format(x))
