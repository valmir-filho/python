"""
Funções decoradoras e decoradores no Python.

No Python, as funções decoradoras (decorators) são um recurso poderoso e flexível que permite modificar o comportamento de outras funções ou métodos sem alterá-los diretamente. Decoradores são frequentemente usados para adicionar funcionalidades extras, como registro, validação, autorização, entre outras, a funções existentes. Eles são usados com a sintaxe "@" antes de uma função que você deseja decorar.

Aqui estão alguns pontos-chave sobre decoradores no Python:

- Sintaxe de decorador: os decoradores são definidos como funções que recebem outra função como argumento. Eles geralmente definem uma função interna que envolve a função original e modifica seu comportamento.

- Aplicação de decoradores: decoradores são aplicados usando a notação "@" antes da definição da função que você deseja decorar.

- Ordem de execução: os decoradores são aplicados na ordem em que são definidos. Isso significa que, se você tiver vários decoradores aplicados a uma função, eles serão executados na ordem em que aparecem de cima para baixo.

- Uso comuns de decoradores: decoradores são comumente usados para fins como controle de acesso, registro, medição de tempo, validação de argumentos e outras tarefas de gerenciamento de funções.

Python também inclui alguns decoradores internos úteis, como "@staticmethod", "@classmethod" e "@property" para trabalhar com métodos de classe e propriedades. Além disso, existem bibliotecas e frameworks que fornecem decoradores prontos para uso para tarefas específicas.

Decoradores são uma ferramenta poderosa e flexível no Python, que pode ser usada para tornar seu código mais modular, legível e reutilizável. Eles são um conceito avançado, mas uma compreensão sólida de como funcionam pode melhorar muito a sua capacidade de escrever código eficiente e limpo no Python.
"""


def meu_decorador(funcao):
    def wrapper():
        print("Antes de chamar a função.")
        funcao()
        print("Depois de chamar a função.")
    return wrapper


@meu_decorador
def minha_funcao():
    print("Minha função.")


minha_funcao()

"""
Neste exemplo, "meu_decorador" é um decorador personalizado que envolve a função "minha_funcao". Quando você chama "minha_funcao()", na verdade está chamando a função decorada, "wrapper", que imprime mensagens antes e depois de chamar "minha_funcao()".
"""
