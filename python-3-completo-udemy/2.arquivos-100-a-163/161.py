"""
Configurações do decorator dataclass no Python.

O decorador "dataclass" do Python é bastante flexível e oferece várias opções de configuração para personalizar o comportamento da classe de dados. Aqui estão
algumas das configurações mais comuns e úteis:

1) "init"

    - Descrição: se "True", um método "__init__()" é adicionado à classe.
    - Uso Padrão: "True".
    - Exemplo: "@dataclass(init=False)" para não gerar automaticamente um método "__init__()".

2) "repr"

    - Descrição: se "True", um método "__repr__()" é adicionado para fornecer uma representação de string da classe.
    - Uso Padrão: "True".
    - Exemplo: "@dataclass(repr=False)" para não criar um método "__repr__()".

3) "eq"
    - Descrição: se "True", métodos "__eq__()" e "__ne__()" são adicionados, permitindo comparação de igualdade entre instâncias.
    - Uso Padrão: "True".
    - Exemplo: "@dataclass(eq=False)" para desabilitar a comparação de igualdade.

4) "order"
    - Descrição: se "True", adiciona métodos "__lt__", "__le__", "__gt__", e "__ge__", permitindo comparação de ordem entre instâncias.
    - Uso Padrão: "False".
    - Exemplo: "@dataclass(order=True)" para permitir comparações como menor que e maior que.

5) "unsafe_hash"
    - Descrição: se "True", um método "__hash__()" é adicionado à classe. Isso é útil se você precisa que instâncias da sua classe de dados sejam usáveis como chaves em dicionários ou em conjuntos.
    - Uso Padrão: determinado automaticamente. É "True" se "eq" for "True" e "frozen" for "True".
    - Exemplo: "@dataclass(unsafe_hash=True)" para forçar a adição de um método "__hash__()".

6) "frozen"
    - Descrição: se "True", torna a instância imutável após a criação. Tentar modificar qualquer atributo resultará em um "FrozenInstanceError".
    - Uso Padrão: "False".
    - Exemplo: "@dataclass(frozen=True)" para criar uma classe de dados imutável.

7) "slots"
    - Descrição: se "True", cria uma classe com "__slots__" definidos, o que pode resultar em um uso de memória mais eficiente.
    - Uso Padrão: "False".
    - Exemplo: "@dataclass(slots=True)" para usar "__slots__" na classe.

8) "kw_only"
    - Descrição: a partir do Python 3.10, se "True", todos os campos são definidos como argumentos de palavra-chave apenas no método "__init__".
    - Uso Padrão: "False".
    - Exemplo: "@dataclass(kw_only=True)" para forçar que todos os argumentos sejam passados como palavras-chave.

Estas opções oferecem uma grande flexibilidade, permitindo que você ajuste o comportamento da sua classe de dados conforme necessário. É importante notar que
algumas dessas opções podem afetar a compatibilidade da sua classe com outras partes do código, especialmente em relação à imutabilidade e à comparação de
instâncias.
"""
