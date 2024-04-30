"""
contextlib.contextmanager no Python.

contextlib.contextmanager é um decorador que permite criar gerenciadores de contexto usando geradores. É uma maneira mais concisa e conveniente de criar
gerenciadores de contexto em Python.
"""

from contextlib import contextmanager

@contextmanager
def meu_gerenciador_de_contexto():
    # Código a ser executado ao entrar no contexto
    print("Entrando no contexto.")
    
    # Realize qualquer inicialização necessária
    recurso = "Recurso inicializado."
    
    try:
        yield recurso  # Retorna o recurso para ser usado dentro do contexto
    finally:
        # Código a ser executado ao sair do contexto
        print("Saindo do contexto.")
        # Realize ações de limpeza, como fechar arquivos, conexões, etc.


# Usando o gerenciador de contexto
with meu_gerenciador_de_contexto() as recurso:
    # Código dentro do contexto
    print("Dentro do contexto.")
    print(f"Recurso: {recurso}")

# Após sair do contexto
print("Fora do contexto.")

"""
Neste exemplo, o decorador "@contextmanager" é usado para criar um gerenciador de contexto chamado "meu_gerenciador_de_contexto". O código a ser executado ao entrar
no contexto é colocado antes do "yield", e o código a ser executado ao sair do contexto é colocado após o "yield" e dentro de um bloco "finally".

Dentro do bloco "with", você pode usar o recurso retornado pelo "yield", e ele estará disponível para uso. Após sair do contexto, o código dentro do bloco "finally"
é executado, permitindo ações de limpeza.

"contextlib.contextmanager" é útil quando você precisa criar gerenciadores de contexto simples e não deseja definir uma classe completa. Ele simplifica a criação e
o uso de gerenciadores de contexto em situações em que uma classe completa é desnecessária.
"""
