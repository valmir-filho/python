# Exercício: crie uma classe, salve os dados em um arquivo JSON, para usá-los posteriormente em um novo módulo Python.

import json


class Pessoa:
    def __init__(
        self,
        nome,
        altura,
        peso,
        raca,
        idade,
        sexo,
        religiao,
        possui_deficiencia
    ):
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.raca = raca
        self.idade = idade
        self.sexo = sexo
        self.religiao = religiao
        self.possui_deficiencia = possui_deficiencia


p1 = Pessoa("Valmir", 1.70, 70, "Branca", 44, "M", "Ateu", False)
p2 = Pessoa("Audi", 1.60, 50, "Branca", 44, "F", "Católica", False)

caminho_arquivo = "/Users/valmirfilho/Downloads/python-3-completo-udemy/aula121/classe.json"
dados = [p1.__dict__, p2.__dict__]

with open(caminho_arquivo, "w") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)
