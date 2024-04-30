"""
Mixins no Python.

Mixins são classes que são projetadas para serem combinadas com outras classes para adicionar funcionalidades específicas sem herança múltipla direta. A herança
múltipla direta (ou seja, herdar de várias classes) pode ser confusa e problemática em muitas linguagens de programação, mas os mixins oferecem uma maneira de
contornar esse problema. Eles são classes que geralmente contêm métodos e atributos, mas não são destinados a serem instanciados por si mesmos.

A ideia principal dos mixins é promover a reutilização de código. Você pode criar uma classe mixin com um conjunto específico de métodos e, em seguida, combinar
essa classe mixin com outras classes para adicionar esses métodos a essas classes.
"""


class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class JsonPerson(JSONMixin, Person):
    pass


person = JsonPerson("Alice", 30)
json_data = person.to_json()
print(json_data)

"""
Neste exemplo, JSONMixin é um mixin que adiciona o método "to_json" para serializar um objeto em JSON. A classe "JsonPerson" combina "JSONMixin" e "Person" para
adicionar a funcionalidade de serialização JSON à classe "Person".
"""
