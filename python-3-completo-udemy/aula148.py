"""
Funções decoradoras e decoradores com classes no Python.

Funções decoradoras e decoradores com classes são maneiras de estender ou modificar o comportamento de funções ou métodos em Python. Decoradores são amplamente
utilizados em Python para adicionar funcionalidades a funções ou métodos existentes de forma limpa e reutilizável.

- Funções Decoradoras: as funções decoradoras são funções que envolvem outras funções ou métodos para adicionar funcionalidades extras.

- Decoradores com Classes: decoradores podem ser implementados usando classes, em vez de funções.

Ambas as abordagens (funções decoradoras e decoradores com classes) são usadas para estender e modificar o comportamento de funções ou métodos de forma limpa e
modular. Você pode escolher a abordagem que melhor se adapta às suas necessidades e preferências.
"""

# Exemplo de função decoradora

import time


def medir_tempo_de_execucao(funcao):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f"A função {funcao.__name__} levou {fim - inicio:.4f} segundos para ser executada.")
        return resultado
    return wrapper


@medir_tempo_de_execucao
def funcao_demorada1():
    # Simula uma função demorada
    time.sleep(2)

funcao_demorada1()

"""
Neste exemplo, "medir_tempo_de_execucao" é uma função decoradora que envolve "funcao_demorada1". Quando chamamos "funcao_demorada1()", a função decoradora mede o
tempo de execução e imprime o resultado.
"""

# Exemplo de decorador com classe


class MeuDecoradorComClasse:
    def __init__(self, funcao):
        self.funcao = funcao

    def __call__(self, *args, **kwargs):
        inicio = time.time()
        resultado = self.funcao(*args, **kwargs)
        fim = time.time()
        print(f"A função {self.funcao.__name__} levou {fim - inicio:.4f} segundos para ser executada.")
        return resultado


@MeuDecoradorComClasse
def funcao_demorada2():
    # Simula uma função demorada
    time.sleep(2)

funcao_demorada2()

"""
Neste exemplo, "MeuDecoradorComClasse" é uma classe que atua como um decorador. Ela envolve a função "funcao_demorada2" e mede o tempo de execução da mesma forma
que o exemplo anterior com funções decoradoras.
"""
