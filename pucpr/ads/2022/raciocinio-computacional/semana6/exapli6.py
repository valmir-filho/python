# Unidade 06: Funções
"""Documentar os códigos é uma boa prática de desenvolvimento. Especificamente no caso de funções, a documentação dentro
de um padrão específico permite, com ferramental extra, a criação de documentação automática, gerada a partir das
informações cadastradas. Da mesma forma, com o padrão correto, o PyCharm consegue ler internamente a descrição das
funções, gerando uma ajuda que pode ser acessada internamente no projeto. O desenvolvimento em Python é regido por
alguns documentos de boas práticas, chamados Python Enhancement Proposals (PEPs). No caso da documentação, existe o
padrão docstrings, registrado pelo PEP 257 — Docstring Conventions. Cabe destacar que, para os usuários do PyCharm,
ambiente de desenvolvimento integrado (IDE) da empresa JetBrains, esse padrão de documentação pode ser gerado
automaticamente. Para tanto, na primeira linha da função após ela estar completa, devem ser digitadas três aspas
seguidas para comentário de várias linhas e pressionar Enter."""

# Exemplo de aplicação 6: tomando por base o exemplo de aplicação 4, elabore a documentação no padrão PEP 257 da função.

def valores(*numeros):
    """
    Recebe uma lista aleatória de números e calcula o maior e o menor deles.

    :param numeros: lista de números a serem analisados.
    :return: retorna o maior e o menor número da lista.
    """
    maior = -1000000
    menor = 1000000
    for numero in numeros:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    return maior, menor
resultado = valores(7,15,3,22,1,8)
print('O maior número é: {} e o menor número é: {}.'.format(resultado[0], resultado[1]))
