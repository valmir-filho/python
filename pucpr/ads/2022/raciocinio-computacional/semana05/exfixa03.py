# Unidade 05: Estrutura de dados: tuplas e dicionários
"""Exercício de fixação 3: Crie um programa que cadastre locais históricos do mundo com as suas coordenadas, fazendo uso de
tuplas com parâmetros nomeados. Dica: use a função namedtuple()."""

from collections import namedtuple

monumentos = []
Monumento = namedtuple("Monumento", ["nome", "latitude", "longitude"])
while True:
    nome = input("Nome do monumento: ")
    latitude = float(input("Latitude do monumento: "))
    longitude = float(input("Longitude do monumento: "))
    monumento = Monumento(nome=nome, latitude=latitude, longitude=longitude)
    monumentos.append(monumento)
    if input("Gostaria de cadastrar mais um monumento? (s/n) ") == "n":
        break
for monumento in monumentos:
    print(f"Monumento: {monumento.nome}")
    print(f"Coordenadas: ({monumento.latitude}, {monumento.longitude})")
