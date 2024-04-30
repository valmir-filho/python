"""
docstring em classes no Python.

Usar docstrings em classes é uma prática recomendada para tornar seu código mais legível e compreensível, especialmente quando você compartilha seu código com
outros desenvolvedores. Além disso, essas docstrings podem ser usadas para gerar documentação automática, se desejar.
"""


class MinhaClasse:

    """
    Esta é a docstring da classe MinhaClasse.

    A classe MinhaClasse tem a seguinte funcionalidade:
    - ...
    - ...

    Atributos:
        atributo1: Uma descrição do primeiro atributo.
        atributo2: Uma descrição do segundo atributo.

    Métodos:
        metodo1(): Descrição do método 1.
        metodo2(parametro): Descrição do método 2.
    """

    def __init__(self, atributo1, atributo2):
        self.atributo1 = atributo1
        self.atributo2 = atributo2

    def metodo1(self):

        """
        Este é o docstring do método 1.

        Descrição mais detalhada do que o método 1 faz.
        """

        # Corpo do método aqui
        pass

    def metodo2(self, parametro):

        """
        Este é o docstring do método 2.

        Args:
            parametro: Uma descrição do parâmetro do método.

        Returns:
            O valor retornado pelo método.
        """

        # Corpo do método aqui
        return ...


"""
Neste exemplo, a docstring da classe "MinhaClasse" fornece uma descrição geral da classe, bem como informações sobre os atributos e métodos da classe. Cada método
também possui sua própria docstring que descreve sua funcionalidade, os argumentos que aceita (caso haja) e o que retorna (se aplicável).
"""

# Você pode acessar a docstring de uma classe usando o atributo ".__doc__".

print(MinhaClasse.__doc__)

# Você pode acessar a docstring de um método específico da classe

print(MinhaClasse.metodo1.__doc__)
