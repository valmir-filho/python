"""
Classes no Python.

No Python, uma classe é um modelo ou template para criar objetos. Objetos são instâncias de uma classe e podem ter atributos (variáveis) e métodos (funções). Classes fornecem uma maneira de modelar e organizar dados e funcionalidades de maneira estruturada e reutilizável. Python é uma linguagem de programação orientada a objetos (POO), e classes são um conceito fundamental na POO.

Por convenção, os nomes das classes usam PascalCase (também conhecido como UpperCamelCase):

- O nome da classe começa com uma letra maiúscula.
- Se a classe possuir um nome composto, cada palavra subsequente começa com uma letra maiúscula, sem espaços ou outros caracteres de separação.

Definindo uma classe: para criar uma classe, você usa a palavra-chave "class", seguida do nome da classe. Você também pode especificar uma classe base (também conhecida como superclasse) se a sua classe herdar de outra classe.

Exemplo:
class MinhaClasse:
    # Atributos e métodos da classe vão aqui

Atributos: atributos são variáveis associadas a uma classe. Eles armazenam dados que pertencem à classe e às suas instâncias. Atributos de classe são compartilhados por todas as instâncias da classe, enquanto os atributos de instância são exclusivos de cada instância.

Exemplo:
class MinhaClasse:
    atributo_de_classe = 0  # Atributo de classe

    def __init__(self, atributo_de_instancia):
        self.atributo_de_instancia = atributo_de_instancia  # Atributo de instância

Métodos: métodos são funções definidas dentro de uma classe. Eles definem o comportamento da classe e de suas instâncias. Normalmente, você tem métodos que manipulam atributos ou realizam alguma ação.

Exemplo:
class MinhaClasse:
    def __init__(self, valor):
        self.valor = valor

    def exibir_valor(self):
        print(f"Valor: {self.valor}.")

Instanciando objetos: para criar um objeto (uma instância de uma classe), você chama a classe como se fosse uma função, passando os argumentos necessários para o método "__init__" da classe.

Exemplo:
obj1 = MinhaClasse(10)
obj2 = MinhaClasse(20)

Acessando atributos e métodos: você pode acessar os atributos e métodos do objeto usando a notação de ponto.

Exemplo:
print(obj1.valor)  # Acessando atributo
obj2.exibir_valor()  # Chamando método

Herança: Python suporta herança de classes, o que permite criar novas classes com base em classes existentes. A herança é uma maneira de reutilizar e estender a funcionalidade de uma classe base.

Exemplo:
class MinhaSubclasse(MinhaClasse):
    def novo_metodo(self):
        print("Novo método na subclasse.")

Encapsulamento: Python fornece diferentes níveis de encapsulamento para membros de classe. Por convenção, atributos e métodos com um prefixo de sublinhado simples (por exemplo, "_atributo_interno") são considerados "protegidos" e aqueles com dois sublinhados (por exemplo, "__atributo_privado") são considerados "privados".

Métodos especiais: Python possui um conjunto de métodos especiais, frequentemente chamados de métodos "mágicos" ou "dunder" (abreviação de "double underscore"), que são identificados por sublinhados duplos em ambos os lados (por exemplo, "__init__", "__str__", "__eq__"). Esses métodos definem como os objetos da classe se comportam em vários contextos, como representação de string ou comparações.

As classes são essenciais para organizar e estruturar código em projetos Python maiores e para implementar estruturas de dados e comportamentos complexos. Elas promovem a reutilização de código, modularidade e manutenibilidade.
"""
