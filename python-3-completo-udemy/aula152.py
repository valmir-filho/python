"""
Metaclasses no Python.

No Python, as metaclasses podem ser vistas como classes especiais que controlam o comportamento e a criação de outras classes. Em outras palavras, uma metaclasse é
uma classe que define como outras classes são criadas e se comportam. Elas desempenham um papel fundamental na metaprogramação, permitindo que você personalize a
criação de classes e adicione comportamentos específicos às classes que estão sendo criadas.

Para entender melhor o conceito de metaclasses, é útil saber que, no Python, as classes são objetos, e esses objetos têm classes próprias. O tipo de uma classe é
chamado de sua metaclasse. Por padrão, a metaclasse de uma classe é a classe "type", que é uma metaclasse embutida em Python.

Você pode criar suas próprias metaclasses definindo uma classe que herda de "type" e personalizando seu comportamento, especialmente o método "__new__", que é
chamado quando uma nova classe está sendo criada. Ao fazer isso, você pode adicionar lógica personalizada, como a validação de atributos, a injeção de métodos ou a
alteração do comportamento da classe.
"""
