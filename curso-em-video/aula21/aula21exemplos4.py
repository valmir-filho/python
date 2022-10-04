# Escopo de variáveis

def funcao():
    n1 = 4  # variável de escopo local.
    print(f'n1 dentro vale {n1}.')


n1 = 2  # variável de escopo global.
funcao()
print(f'n1 fora vale {n1}.')
