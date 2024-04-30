"""
__dict__ no Python.

É um atributo especial que contém um dicionário (um tipo de estrutura de dados) que mapeia os atributos (variáveis) de uma instância de uma classe para seus valores. É uma maneira de acessar os atributos de um objeto diretamente, como se eles fossem elementos de um dicionário.

Aqui estão os conceitos-chave relacionados ao "__dict__":

- Atributos de um objeto: no Python, os objetos têm atributos que são variáveis associadas a eles. Esses atributos podem ser definidos na classe ou na instância do objeto.

- __dict__ acessa os atributos: o atributo "__dict__" de um objeto contém um dicionário que mapeia o nome dos atributos aos seus valores. Isso inclui todos os atributos do objeto, independentemente de onde ou como eles foram definidos.

- Uso prático: acesso direto ao "__dict__" não é comum em código Python do dia a dia. É mais utilizado para fins de introspecção, depuração ou para situações específicas em que você deseja acessar ou manipular os atributos de um objeto dinamicamente.

- Limitações: o uso do "__dict__" pode ser limitado em certos casos, como quando os atributos são definidos com duplo sublinhado (ex: "__atributo_privado") ou quando a classe usa "__slots__" para restringir a criação dinâmica de atributos. Além disso, não é a maneira mais eficiente de acessar atributos, portanto, é preferível usar a notação de ponto padrão (por exemplo, "objeto.atributo") sempre que possível.

Em resumo, o "__dict__" no Python é um atributo especial que permite acessar um dicionário contendo todos os atributos e seus valores de um objeto. Embora possa ser útil em situações específicas, seu uso direto não é comum na programação cotidiana. É mais comumente usado para introspecção e depuração.
"""

# Exemplo


class Exemplo:
    def __init__(self):
        self.atributo1 = 10
        self.atributo2 = "Texto"


objeto = Exemplo()

# Acessando os atributos usando o __dict__
print(objeto.__dict__)

# Acessando os atributos usando o vars()
atributos = vars(objeto)
print(atributos)
