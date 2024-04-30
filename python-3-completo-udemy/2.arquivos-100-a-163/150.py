"""
Método especial "__call__" no Python.

O método especial "__call__" é um recurso poderoso no Python que permite que um objeto seja chamado como uma função. Quando você define o método "__call__" em uma
classe, você está essencialmente tornando objetos dessa classe invocáveis, como funções. Isso pode ser útil para criar objetos que compartilham comportamentos
semelhantes aos de funções ou para adicionar funcionalidades extras a instâncias da classe.
"""


class MinhaClasse:
    def __init__(self, valor):
        self.valor = valor

    def __call__(self, x):
        # Este método será chamado quando uma instância da classe for usada como uma função
        return self.valor * x


# Criando uma instância da classe
obj = MinhaClasse(10)

# Agora, podemos chamar a instância como uma função
resultado = obj(5)
print(resultado)  # Isso imprimirá 50

# Podemos chamar a instância novamente como uma função
resultado2 = obj(8)
print(resultado2)  # Isso imprimirá 80

"""
Neste exemplo, a classe "MinhaClasse" possui um método "__call__", que é responsável por executar a ação quando uma instância da classe é chamada como uma função.
Quando "obj(5)" é chamado, o método "__call__" é acionado, multiplicando "self.valor" por "x", resultando em 50.

O método "__call__" é útil quando você deseja criar objetos que compartilham comportamentos semelhantes aos de funções e desejam manter um estado interno, que é
útil para manter informações entre chamadas. É uma forma de adicionar uma interface funcional a objetos.
"""
