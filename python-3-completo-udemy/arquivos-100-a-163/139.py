"""
Polimorfismo, assinatura de métodos e princípio da substituição de Liskov no Python.

O polimorfismo, a assinatura de métodos e o Princípio da Substituição de Liskov (Liskov Substitution Principle - LSP) são conceitos fundamentais na programação
orientada a objetos (POO) e estão intrinsecamente relacionados.

Polimorfismo:
   
- O polimorfismo é um dos princípios fundamentais da POO e significa "muitas formas". Ele permite que objetos de diferentes classes sejam tratados como objetos de
uma classe comum por meio de herança e interfaces. O polimorfismo permite que você chame métodos em um objeto, independentemente de qual classe concreta a
instância pertence, desde que a classe tenha uma interface compatível.

- No polimorfismo, as classes derivadas (subclasses) podem substituir os métodos da classe base (superclasse) para fornecer comportamento específico. Isso é
fundamental para a flexibilidade e extensibilidade do código.

Assinatura de Métodos:
   
- A assinatura de um método refere-se à sua lista de parâmetros, incluindo seus tipos e ordem. A assinatura de método é um identificador
exclusivo para o método. Em POO, dois métodos na mesma classe não podem ter a mesma assinatura, pois isso levaria a ambiguidade.

- Exemplo de assinatura de método: "int calcularArea(int largura, int altura);".

Princípio da Substituição de Liskov (LSP):

- O Princípio da Substituição de Liskov é um dos cinco princípios SOLID da programação orientada a objetos, proposto por Barbara Liskov.
Ele estabelece que objetos de uma classe derivada (subclasse) devem ser capazes de substituir objetos da classe base (superclasse) sem que o
programa se comporte de maneira incorreta.

- Isso significa que, ao herdar de uma classe base, uma classe derivada deve respeitar a assinatura dos métodos da classe base e não deve
alterar seu comportamento de forma que viole as expectativas dos clientes da classe base.

- Em termos simples, a LSP garante que a herança seja usada de maneira que as subclasses possam ser substituídas pelas superclasses sem
problemas.

- Um exemplo clássico em que a LSP é violada é quando uma subclasse modifica o comportamento da classe base, como lançando exceções
inesperadas ou retornando resultados incompatíveis.

- A relação entre esses conceitos está na aplicação do polimorfismo. Ao escrever código polimórfico, você permite que diferentes subclasses
(com assinaturas de métodos compatíveis) sejam usadas de maneira intercambiável, cumprindo assim o Princípio da Substituição de Liskov.

Em resumo, o polimorfismo permite que objetos de diferentes classes se comportem de maneira semelhante, desde que respeitem a assinatura dos
métodos da classe base, o que, por sua vez, garante o cumprimento do Princípio da Substituição de Liskov. Isso torna o código mais flexível,
extensível e de fácil manutenção em sistemas orientados a objetos.
"""

"""
Exemplo: imagine que estamos trabalhando com figuras geométricas, como círculos e retângulos. Queremos calcular a área de diferentes formas geométricas usando
polimorfismo. Para isso, criaremos uma classe base chamada "Shape" com um método "calculate_area()". Em seguida, criaremos duas subclasses, "Circle" e "Rectangle",
que herdarão da classe "Shape" e implementarão o método "calculate_area()" de maneira específica para cada forma.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def calculate_area(self):
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def calculate_area(self):
        return self.width * self.height


# Função genérica para calcular a área de qualquer forma
def calculate_shape_area(shape):
    return shape.calculate_area()


# Criação de objetos de diferentes formas
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Cálculo e impressão das áreas usando polimorfismo
print("Área do círculo:", calculate_shape_area(circle))
print("Área do retângulo:", calculate_shape_area(rectangle))

"""
Explicações:
- Definimos uma classe abstrata "Shape" com um método abstrato "calculate_area()". Isso estabelece a assinatura do método para calcular a área de qualquer forma
geométrica.

- Criamos duas subclasses, "Circle" e "Rectangle", que herdam de "Shape". Cada uma dessas subclasses fornece uma implementação concreta do método
"calculate_area()", específica para a forma geométrica.

- Usamos uma função genérica "calculate_shape_area()" que aceita qualquer objeto "Shape" como argumento e calcula a área usando polimorfismo.

- Criamos objetos de círculo e retângulo e calculamos suas áreas usando a função genérica. Isso demonstra como objetos de diferentes subclasses podem ser tratados
de maneira semelhante, graças ao polimorfismo.

Esse exemplo ilustra o uso do polimorfismo para calcular áreas de diferentes formas geométricas, respeitando o Princípio da Substituição de Liskov, pois as
subclasses "Circle" e "Rectangle" substituem a implementação do método "calculate_area()" da classe base "Shape".
"""
