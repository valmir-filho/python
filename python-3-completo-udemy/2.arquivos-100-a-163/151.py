"""
Classes decoradoras no Python.

As classes decoradoras no Python são uma forma de aplicar padrões de design de decoradores a funções ou métodos. Decoradores são funções que recebem outra função e
estendem ou modificam seu comportamento sem alterar o código-fonte original. Decoradores são comumente usados em Python para realizar tarefas como registro de
funções, autorização de acesso, cálculo de tempo de execução e muitas outras funcionalidades de extensão.

Decoradores são normalmente definidos como funções, mas também podem ser definidos como classes.
"""


class MinhaClasseDecoradora:
    def __init__(self, função):
        self.função = função

    def __call__(self, *args, **kwargs):
        # Código a ser executado antes de chamar a função decorada
        print("Antes de chamar a função.")
        
        resultado = self.função(*args, **kwargs)
        
        # Código a ser executado depois de chamar a função decorada
        print("Depois de chamar a função.")
        
        return resultado


@MinhaClasseDecoradora
def minha_função():
    print("Função decorada.")


minha_função()

"""
No exemplo acima, criamos uma classe "MinhaClasseDecoradora" que recebe uma função como argumento em seu construtor e a armazena em "self.função". A classe também
define um método "__call__", que é chamado quando tentamos chamar a função decorada. Nesse método, você pode adicionar código que será executado antes e depois de
chamar a função original.

Em seguida, aplicamos essa classe decoradora à função "minha_função" usando a notação "@MinhaClasseDecoradora". Quando chamamos "minha_função()", a classe
decoradora se encarregará de executar o código antes e depois da função decorada, conforme mostrado nas mensagens de impressão.

Classes decoradoras podem ser úteis quando você precisa realizar tarefas mais complexas em seus decoradores ou manter um estado interno entre as chamadas à função
decorada. No entanto, na maioria dos casos, decoradores baseados em funções são mais simples e amplamente usados.
"""
