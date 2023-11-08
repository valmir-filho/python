"""
docstring em funções no Python.

No Python, os docstrings são strings literais que aparecem como o primeiro item em uma definição de função, classe, módulo ou método. O principal propósito dos
docstrings é fornecer documentação embutida para o código, facilitando a compreensão do código e seu uso por outros desenvolvedores.

A docstring geralmente inclui os seguintes elementos:

- Uma breve descrição da função ou método.
- Uma seção "Args" que lista os parâmetros da função e fornece descrições de cada um deles.
- Uma seção "Returns" que descreve o que a função retorna, se aplicável.
- Outras seções, como "Raises" para listar exceções que a função pode lançar, ou qualquer outra informação relevante.

É uma prática recomendada usar docstrings para documentar suas funções, classes e métodos, pois isso torna seu código mais legível e facilita a colaboração com
outros desenvolvedores. Além disso, ferramentas como o Sphinx podem gerar documentação a partir das docstrings para criar uma documentação mais formal para seu
projeto.
"""


def minha_funcao(parametro1, parametro2):
    
    """
    Esta é a descrição da minha_funcao.

    Args:
        parametro1: Uma descrição do primeiro parâmetro.
        parametro2: Uma descrição do segundo parâmetro.

    Returns:
        O valor retornado pela função.
    """

    # Corpo da função aqui
    return ...


"""
Neste exemplo, a docstring é a string multilinha entre as três aspas duplas logo abaixo da assinatura da função. Você pode usar docstrings de uma linha
(entre aspas simples ou duplas) ou docstrings multilinhas (entre três aspas simples ou três aspas duplas), dependendo da complexidade da documentação que deseja
incluir.
"""

# Você pode acessar a docstring de uma função em tempo de execução usando o atributo ".__doc__".

print(minha_funcao.__doc__)
