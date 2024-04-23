# Escopo de variáveis

def funcao():
    global n1  # esse comando serve para considerar apenas o valor da variável de escopo global.
    n1 = 4  # variável de escopo local.
    print(f'n1 dentro vale {n1}.')


n1 = 2  # variável de escopo global.
funcao()
print(f'n1 fora vale {n1}.')
