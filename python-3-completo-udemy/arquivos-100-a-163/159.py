"""
Dataclasses no Python.

As dataclasses no Python são uma funcionalidade introduzida na versão 3.7 que proporciona uma maneira mais simples e menos verbosa de criar classes, especialmente
aquelas usadas principalmente para armazenar dados. Elas são úteis para criar classes que se assemelham a estruturas de dados ou "registros".

1) Características das Dataclasses:

- Simplificação da Definição de Classes: antes das dataclasses, a criação de classes para armazenar dados exigia a escrita manual de métodos como "__init__",
"__repr__", "__eq__", entre outros. As dataclasses automatizam isso.

- Decorador @dataclass: você utiliza o decorador @dataclass do módulo dataclasses para transformar sua classe em uma dataclass. Isso instrui o Python a adicionar
automaticamente métodos especiais à classe.

- Métodos Especiais Automáticos: uma dataclass automaticamente gera métodos como "__init__()", "__repr__()", e "__eq__()" com base nos atributos definidos na classe.
Isso economiza tempo e evita erros comuns.

- Tipagem e Valores Default: as dataclasses suportam type hints e permitem definir valores default para os atributos, o que melhora a legibilidade e a consistência
do código.
"""

from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

    def total_cost(self) -> float:
        return self.price * self.quantity


# Uso da dataclass
product = Product(name="Laptop", price=1000.00)
print(product)           # Saída automática formatada
print(product.total_cost())

"""
2) Vantagens das Dataclasses:

- Menos Código e Mais Clareza: Reduz a necessidade de métodos boilerplate, tornando o código mais limpo e fácil de entender.

- Imutabilidade Opcional: Você pode tornar uma dataclass imutável (somente leitura) usando o parâmetro frozen.

- Facilita a Comparação de Objetos: Com métodos como "__eq__" gerados automaticamente, a comparação de objetos torna-se trivial.

- Integração com Outras Funcionalidades: Dataclasses trabalham bem com outras funcionalidades do Python, como typing e default factories.

3) Considerações:

- As dataclasses são mais adequadas para classes que armazenam principalmente dados e têm pouca lógica de negócios.

Para funcionalidades mais complexas, como validação de dados ou métodos personalizados, você pode precisar escrever código adicional além do gerado automaticamente.

As dataclasses são uma adição poderosa ao Python, fornecendo uma maneira mais eficiente e legível de criar classes orientadas a dados.
"""
