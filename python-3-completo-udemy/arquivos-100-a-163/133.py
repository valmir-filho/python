""" 
Herança múltipla no Python.

A herança múltipla é um recurso no Python que permite que uma classe herde atributos e métodos de várias classes diferentes. Isso significa que uma classe pode
ter várias classes base (ou superclasses) das quais ela herda funcionalidades. A herança múltipla é uma característica poderosa, mas também pode ser complexa,
e é importante usá-la com cuidado para evitar conflitos e ambiguidades.
"""

# Exemplo


class ClasseA:
    def metodo_a(self):
        print("Método da ClasseA.")


class ClasseB:
    def metodo_b(self):
        print("Método da ClasseB.")


class ClasseC(ClasseA, ClasseB):
    def metodo_c(self):
        print("Método da ClasseC.")


objeto_c = ClasseC()

objeto_c.metodo_a()  # Chama o método da ClasseA
objeto_c.metodo_b()  # Chama o método da ClasseB
objeto_c.metodo_c()  # Chama o método da ClasseC

print(ClasseC.mro())

"""
Neste exemplo, "ClasseC" herda de tanto "ClasseA" quanto "ClasseB". Isso significa que "ClasseC" possui os métodos "metodo_a" e "metodo_b" da "ClasseA" e "ClasseB",
respectivamente, além de seu próprio método "metodo_c".

No entanto, a herança múltipla pode levar a conflitos se as classes base tiverem métodos ou atributos com o mesmo nome. Para resolver tais conflitos, Python segue
uma ordem de pesquisa de método chamada MRO (Method Resolution Order) usando o algoritmo C3 Linearization. Isso determina a ordem em que as classes base são
pesquisadas quando você chama um método em uma classe derivada.

Para saber a ordem de resolução de método de uma classe, você pode usar o atributo ".__mro__" ou a função "mro()".

É importante lembrar que, devido à complexidade da herança múltipla, é aconselhável evitá-la sempre que possível e usar a composição e a interface mais simples em
seu lugar. O uso excessivo da herança múltipla pode tornar o código difícil de entender e manter.
"""
