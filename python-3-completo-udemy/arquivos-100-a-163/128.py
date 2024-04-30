"""
Encapsulamento no Python.

O encapsulamento no Python refere-se à prática de esconder os detalhes internos de uma classe ou objeto e fornecer uma interface pública para interagir com ele.
Isso ajuda a promover a modularidade e a ocultação de informações, tornando o código mais robusto e menos suscetível a erros causados por alterações acidentais
nas partes internas de um objeto.

No Python, o encapsulamento é alcançado principalmente por meio de convenções de nomenclatura e pelo uso de modificadores de acesso.

Existem três tipos principais de modificadores de acesso em Python:

- Público: métodos e atributos que não têm prefixos especiais são considerados públicos e podem ser acessados de fora da classe. Por exemplo:

- Protegido: os atributos e métodos que começam com um sublinhado simples, como "_nome", são considerados protegidos. Isso é uma convenção para informar aos
programadores que esses elementos não devem ser acessados diretamente de fora da classe, mas eles ainda podem ser acessados se necessário.

- Privado: os atributos e métodos que começam com dois sublinhados duplos, como "__nome", são considerados privados. Eles são fortemente encapsulados e não devem
ser acessados de fora da classe. No entanto, em Python, ainda é possível acessá-los, mas de uma maneira ligeiramente diferente.

Para acessar atributos e métodos protegidos ou privados de fora da classe, você pode fazê-lo, mas não é uma prática recomendada. O encapsulamento no Python é,
em grande parte, baseado na confiança dos programadores para respeitar as convenções e não acessar diretamente o que é destinado a ser protegido.

O encapsulamento ajuda a manter a integridade e a consistência de um objeto, tornando-o mais fácil de usar e de manter, bem como evita a exposição acidental de
detalhes de implementação que podem ser alterados no futuro.
"""

# Exemplo de um método público


class MinhaClasse:
    def __init__(self):
        self.publico_atributo = 42

    def metodo_publico(self):
        return "Este é um método público."
    

# Exemplo de um método protegido


# class MinhaClasse:
#     def __init__(self):
#         self._atributo_protegido = 42

#     def _metodo_protegido(self):
#         return "Este é um método protegido."


# Exemplo de um método privado


# class MinhaClasse:
#     def __init__(self):
#         self.__atributo_privado = 42

#     def __metodo_privado(self):
#         return "Este é um método privado."

#     def acessar_metodo_privado(self):
#         return self.__metodo_privado()
