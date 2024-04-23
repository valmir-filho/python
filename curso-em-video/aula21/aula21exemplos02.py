# Docstrings

def contador(i, f, p):
    """
    A função contador faz uma contagem e mostra na tela.
    :param i: parâmetro de início da contagem.
    :param f: parâmetro de fim da contagem.
    :param p: passo da contagem.
    :return: não retorna nada.
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fim!')


contador(2, 10, 2)
print()
help(contador)
