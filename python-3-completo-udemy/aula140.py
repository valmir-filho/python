"""
Criação de exceções no Python.

No Python, você pode criar suas próprias exceções personalizadas (classes de exceção) ao estender a classe base "Exception" ou qualquer uma das suas subclasses.
Isso permite que você crie exceções personalizadas para lidar com situações específicas em seu código.

- Definindo uma exceção personalizada: para criar uma exceção personalizada, você precisa definir uma classe que herda de "Exception" ou de outra classe de exceção
existente. Você pode adicionar métodos e atributos à sua classe de exceção, se necessário.

Exemplo:


class MinhaExcecaoPersonalizada(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


- Neste exemplo, criamos uma exceção personalizada chamada "MinhaExcecaoPersonalizada" que herda de "Exception". O construtor "__init__" aceita uma mensagem de
erro que será exibida quando a exceção for levantada.

- Levantando a exceção personalizada: quando ocorre uma condição que requer a ativação da exceção personalizada, você pode levantá-la usando a instrução "raise".
Você pode passar uma instância da sua exceção personalizada e opcionalmente uma mensagem de erro.

Exemplo:

raise MinhaExcecaoPersonalizada("Isso é uma exceção personalizada!")

- Isso levantará a exceção personalizada com a mensagem especificada.

- Capturando a exceção personalizada: para capturar e lidar com exceções personalizadas, você pode usar um bloco "try" e "except" em torno do código que pode
levantar a exceção. No bloco "except", você especifica o tipo da exceção personalizada que deseja tratar.

Exemplo:

try:
    # Código que pode levantar a exceção personalizada
    raise MinhaExcecaoPersonalizada("Isso é uma exceção personalizada!")
except MinhaExcecaoPersonalizada as e:
    print("Exceção capturada:", e)

- Neste exemplo, estamos capturando a exceção personalizada "MinhaExcecaoPersonalizada" e imprimindo a mensagem de erro associada à exceção.
"""

# Exemplo completo


class MinhaExcecaoPersonalizada(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


try:
    # Simulando uma situação que requer uma exceção personalizada
    raise MinhaExcecaoPersonalizada("Isso é uma exceção personalizada!")
except MinhaExcecaoPersonalizada as e:
    print("Exceção capturada:", e)

"""
Esse código cria e manipula uma exceção personalizada, demonstrando como você pode definir exceções sob medida para suas necessidades e como capturá-las para
tratamento específico.
"""
