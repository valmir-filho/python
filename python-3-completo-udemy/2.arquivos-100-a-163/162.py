"""
"asdict()" e "astuple()" no Python.

As funções "asdict()" e "astuple()" são duas utilidades importantes fornecidas pelo módulo "dataclasses" no Python, que facilitam a conversão de instâncias de data
classes para dicionários e tuplas, respectivamente.
"""

"""
"asdict()": converte uma instância de uma data class para um dicionário. Cada campo da data class se torna uma chave no dicionário, com o valor correspondente do
campo como valor no dicionário.
"""

# Exemplo
     
from dataclasses import dataclass, asdict


@dataclass
class Pessoa1:
    nome: str
    idade: int


p = Pessoa1("João", 30)
d = asdict(p)

# Neste exemplo, "d" será "{'nome': 'João', 'idade': 30}".

"""
"astuple()": similar à "asdict()", mas converte a instância da data class para uma tupla. Os valores dos campos da data class são colocados na tupla na mesma ordem
em que são definidos na classe.
"""

# Exemplo

from dataclasses import dataclass, astuple


@dataclass
class Pessoa2:
    nome: str
    idade: int


p = Pessoa2("João", 30)
t = astuple(p)

# Aqui, "t" será "('João', 30)".

"""
Ambas as funções são particularmente úteis para serialização ou para a conversão rápida de uma data class para um formato mais genérico, como dicionário ou tupla.
Isso pode ser prático, por exemplo, ao trabalhar com bibliotecas de serialização JSON ou ao passar dados para funções que esperam estruturas de dados padrão do
Python.

Além disso, "asdict()" e "astuple()" podem lidar com data classes aninhadas, convertendo cada data class aninhada da mesma forma. Por exemplo, se um campo em uma
data class é ele mesmo uma instância de uma data class, "asdict()" converterá esse campo em um dicionário, e "astuple()" o converterá em uma tupla.
"""
