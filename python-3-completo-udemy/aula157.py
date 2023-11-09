"""
Enum no Python.

No Python, a classe "Enum" do módulo "enum" é usada para criar enumeradores, que são uma maneira de criar constantes nomeadas mais legíveis e organizadas.
Enumerações são uma maneira de criar conjuntos de valores nomeados que se comportam como constantes. Elas podem ser usadas para criar código mais legível e menos
propenso a erros, substituindo o uso de constantes numéricas ou strings.
"""

from enum import Enum


class DiaDaSemana(Enum):
    SEGUNDA = 1
    TERCA = 2
    QUARTA = 3
    QUINTA = 4
    SEXTA = 5
    SABADO = 6
    DOMINGO = 7


"""
Neste exemplo, "DiaDaSemana" é uma enumeração que contém sete membros: "SEGUNDA", "TERCA", "QUARTA", "QUINTA", "SEXTA", "SABADO" e "DOMINGO". Cada membro é uma
constante com um valor associado. Os valores padrão são inteiros começando de 1, mas você pode definir valores personalizados se necessário.
"""

# Você pode usar esses membros como constantes no seu código

print(DiaDaSemana.SEGUNDA)  # Saída: DiaDaSemana.SEGUNDA
print(DiaDaSemana.SEGUNDA.value)  # Saída: 1

# Você também pode iterar sobre os membros de uma enumeração

for dia in DiaDaSemana:
    print(dia)

# Você pode comparar membros de enumerações

if DiaDaSemana.SEGUNDA == DiaDaSemana.QUARTA:
    print("Os dois são iguais.")
else:
    print("Os dois são diferentes.")

"""
As enumerações em Python oferecem uma maneira mais legível e segura de lidar com conjuntos específicos de valores. Elas podem ser particularmente úteis em situações
onde você tem um conjunto fixo de opções ou estados possíveis.
"""
