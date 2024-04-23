"""
Exercício com classes.

- Crie uma classe chamada Carro
- Crie uma classe chamada Motor
- Crie uma classe  chamada Fabricante
- Faça a relação: carro tem um motor (obs.: o mesmo motor pode ser de vários carros)
- Faça a relação: carro tem um fabricante (obs.: o mesmo fabricante pode fabricar vários carros)
- Exiba o nome do carro, o motor e o fabricante
"""


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None


    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro("Fusca")
volkswagen = Fabricante("Volkswagen")
motor_1_0 = Motor("1.0")
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

gol = Carro("Gol")
gol.fabricante = volkswagen
gol.motor = motor_1_0
print(gol.nome, gol.fabricante.nome, gol.motor.nome)

fiat_uno = Carro("Uno")
fiat = Fabricante("Fiat")
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0
print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)

focus = Carro("Focus Titanium")
ford = Fabricante("Ford")
motor_2_0 = Motor("2.0")
focus.fabricante = ford
focus.motor = motor_2_0
print(focus.nome, focus.fabricante.nome, focus.motor.nome)