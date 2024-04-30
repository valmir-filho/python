"""
Valores padrão, field e fields em dataclasses no Python.

Em "dataclasses" do Python, os valores padrão e as funções "field()" e "fields()" oferecem controle adicional sobre como os campos são tratados.
"""

"""
1) Valores Padrão em Data Classes: você pode definir valores padrão para os campos em uma data class. Isso é útil quando você quer que um campo tenha um valor
específico se não for explicitamente fornecido na criação da instância.
"""

# Exemplo

from dataclasses import dataclass


@dataclass
class Produto1:
    nome: str
    preco: float = 0.0  # valor padrão para o preço


# Neste caso, se você criar uma instância de "Produto" sem especificar o "preco", ele será automaticamente definido como "0.0".

"""
2) A Função "field()": a função "field()" é usada para fornecer mais informações sobre um campo de uma data class, como métodos de comparação, um valor padrão, ou
se o campo deve ser incluído na representação da classe ("__repr__").
"""

# Exemplo

from dataclasses import dataclass, field


@dataclass
class Produto2:
    nome: str
    preco: float = field(default=0.0, repr=False)  # preço não aparecerá em __repr__


# Aqui, o campo "preco" tem um valor padrão de "0.0", e "repr=False" indica que este campo não será incluído na representação de string da classe.

"""
3) A Função "fields()": a função "fields()" retorna uma tupla de objetos "Field", que são basicamente estruturas que contêm informações sobre cada campo da data
class. Isso é útil para introspecção, ou seja, quando você precisa saber mais sobre os campos de uma data class em tempo de execução.
"""

# Exemplo

from dataclasses import dataclass, field, fields


@dataclass
class Produto3:
    nome: str
    preco: float = 0.0


for f in fields(Produto3):
    print(f.name, f.type)

# Este código percorre todos os campos da classe "Produto" e imprime o nome e o tipo de cada campo.

"""
Esses recursos aumentam a flexibilidade e o poder das data classes no Python, permitindo-lhes serem adaptadas para uma ampla gama de casos de uso, mantendo a
simplicidade e a legibilidade.
"""
