"""
Classes abstratas no Python.

São classes que não podem ser instanciadas diretamente e são usadas como modelos para criar outras classes. Elas são parte do módulo "abc" (Abstract Base Classes)
e fornecem um mecanismo para definir uma estrutura comum para as classes derivadas, estabelecendo um contrato que as classes filhas devem seguir.

A biblioteca "abc" é usada para criar classes abstratas no Python.
"""

"""
Definindo uma classe abstrata: para definir uma classe abstrata, você precisa importar o módulo "abc" e usar a classe "ABC" como base. Além disso, você pode
decorar métodos que deseja que sejam obrigatoriamente implementados nas classes derivadas com o decorador "@abstractmethod".
"""

# Exemplo
from abc import ABC, abstractmethod


class MinhaClasseAbstrata(ABC):
    
    @abstractmethod
    def metodo_abstrato(self):
        pass


# Neste exemplo, "MinhaClasseAbstrata" é uma classe abstrata que define um método abstrato "metodo_abstrato". Classes derivadas devem implementar esse método.

"""
Classes derivadas: para criar uma classe derivada a partir de uma classe abstrata, você deve implementar todos os métodos abstratos definidos na classe base. Caso
contrário, você obterá um erro em tempo de execução.
"""

# Exemplo


class MinhaClasseConcreta(MinhaClasseAbstrata):
    
    def metodo_abstrato(self):
        return "Método implementado na classe concreta."


# Neste exemplo, "MinhaClasseConcreta" é uma classe derivada de "MinhaClasseAbstrata" e implementa o método "metodo_abstrato".

"""
Instanciação de classes derivadas: você pode criar instâncias de classes derivadas, mas não pode criar instâncias de classes abstratas. Tentar criar uma instância
de uma classe abstrata resultará em um erro.
"""

# Exemplo
obj = MinhaClasseConcreta()  # Isso é válido 

# obj = MinhaClasseAbstrata()   # Isso gerará um erro, pois MinhaClasseAbstrata é uma classe abstrata
 
"""
O uso de classes abstratas no Python ajuda a definir uma estrutura comum para várias classes relacionadas, garantindo que métodos específicos estejam disponíveis
em todas as classes derivadas. Isso é especialmente útil quando você deseja impor uma interface comum ou garantir a consistência em um conjunto de classes que têm
funcionalidades similares.
"""
