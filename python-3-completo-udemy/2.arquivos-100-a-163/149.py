"""
Funções decoradoras e decoradores com métodos no Python.

Funções decoradoras e decoradores com métodos em Python podem ser usados para adicionar funcionalidades extras a funções ou métodos de classes de forma reutilizável.
A abordagem é semelhante às funções decoradoras comuns, mas os decoradores com métodos são aplicados a métodos de classe.

Os decoradores também podem ser implementados usando classes que atuam como decoradores para métodos de classe.

Ambas as abordagens (funções decoradoras para métodos e decoradores com métodos de classe) são usadas para estender e modificar o comportamento de métodos de
classes de forma limpa e modular. Você pode escolher a abordagem que melhor se adapta às suas necessidades e preferências.
"""

# Exemplo de funcão decoradora para método (função decoradora que mede o tempo de execução de um método de classe)

import time


def medir_tempo_de_execucao_metodo(metodo):
    def wrapper(self, *args, **kwargs):
        inicio = time.time()
        resultado = metodo(self, *args, **kwargs)
        fim = time.time()
        print(f"O método {metodo.__name__} levou {fim - inicio:.4f} segundos para ser executado.")
        return resultado
    return wrapper


class MinhaClasse1:
    def __init__(self):
        pass

    @medir_tempo_de_execucao_metodo
    def metodo_demorado(self):
        # Simula um método demorado
        time.sleep(2)

obj = MinhaClasse1()
obj.metodo_demorado()

"""
Neste exemplo, "medir_tempo_de_execucao_metodo" é uma função decoradora que envolve o método "metodo_demorado" da classe "MinhaClasse1". Quando chamamos
"obj.metodo_demorado()", a função decoradora mede o tempo de execução do método e imprime o resultado.
"""

# Exemplo de decoradore com métodos de classe

import time


class MeuDecoradorComMetodo:
    def __init__(self, metodo):
        self.metodo = metodo

    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            inicio = time.time()
            resultado = self.metodo(instance, *args, **kwargs)
            fim = time.time()
            print(f"O método {self.metodo.__name__} levou {fim - inicio:.4f} segundos para ser executado.")
            return resultado
        return wrapper


class MinhaClasse2:
    def __init__(self):
        pass

    @MeuDecoradorComMetodo
    def metodo_demorado(self):
        # Simula um método demorado
        time.sleep(2)

obj = MinhaClasse2()
obj.metodo_demorado()

"""
Neste exemplo, "MeuDecoradorComMetodo" é uma classe que atua como um decorador para o método "metodo_demorado" da classe "MinhaClasse2". Ele envolve o método e mede
o tempo de execução da mesma forma que o exemplo anterior com funções decoradoras.
"""
