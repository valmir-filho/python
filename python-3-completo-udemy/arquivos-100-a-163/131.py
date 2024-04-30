"""
Herança no Python.

A herança é um conceito fundamental em programação orientada a objetos (POO), e o Python suporta herança de maneira eficaz. A herança permite que você crie uma
nova classe (subclasse) que herda atributos e métodos de uma classe existente (superclasse ou classe base). Isso promove a reutilização de código e ajuda a
organizar e estruturar o seu código de forma mais eficiente.

Aqui estão os principais pontos sobre herança no Python:

- Definindo uma subclasse: para criar uma subclasse que herda de uma superclasse, você define a subclasse usando a palavra-chave "class", seguida pelo nome da
subclasse e o nome da superclasse em parênteses.

Exemplo:

class Superclasse:
    # Atributos e métodos da superclasse

    
class Subclasse(Superclasse):
    # Atributos e métodos da subclasse


- Herança de atributos e métodos: a subclasse herda todos os atributos (variáveis de instância) e métodos (funções de instância) da superclasse. Isso significa
que você pode usar os atributos e métodos da superclasse na subclasse.

- Adicionando e substituindo métodos: uma subclasse pode adicionar novos métodos ou substituir os métodos herdados da superclasse. Isso permite que a subclasse
personalize o comportamento da superclasse, tornando-a mais específica para suas necessidades.

- Chamando métodos da superclasse: em uma subclasse, você pode chamar métodos da superclasse usando "super()". Isso é útil quando você deseja estender o
comportamento da superclasse em vez de substituí-lo inteiramente.

- Múltipla herança: Python suporta múltipla herança, o que significa que uma subclasse pode herdar de várias superclasses. Isso permite a reutilização de código
de várias fontes. No entanto, a múltipla herança pode ser complexa e deve ser usada com cuidado para evitar conflitos de nomes e confusões.
"""

# Exemplo simples de herança no Python


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Saída: Buddy says Woof!
print(cat.speak())  # Saída: Whiskers says Meow!

""""
Neste exemplo, "Dog" e "Cat" são subclasses da classe "Animal", herdando o método "speak()". Cada subclasse substitui o método "speak()" para personalizar o
comportamento de acordo com o tipo de animal.
"""
