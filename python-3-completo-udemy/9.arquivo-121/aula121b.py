import json

from aula121a import caminho_arquivo, Pessoa

with open(caminho_arquivo, "r") as arquivo:
    pessoas = json.load(arquivo)

p1 = Pessoa(**pessoas[0])
p2 = Pessoa(**pessoas[1])

print(p1.nome)
print(p2.nome)
