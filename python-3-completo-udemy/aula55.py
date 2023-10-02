"""
Valor padrão em funções no Python.

No Python, as funções podem ter argumentos com valores padrão (também conhecidos como argumentos padrão ou argumentos predefinidos).
Valores padrão são valores que são atribuídos automaticamente aos argumentos de uma função se nenhum valor for fornecido quando a função é chamada. Isso permite que você crie funções mais flexíveis e evita a necessidade de fornecer todos os argumentos sempre que a função for usada.
"""


def saudacao(nome, mensagem="Olá"):
    print(f"{mensagem}, {nome}")


saudacao("Valmir", "Bom dia")
saudacao("Valmir")


# def soma(x, y, z=None):
#     print(f"Valores: {x=}, {y=} e {z=} | Soma: {x+y+z}") if z is not None else print(
#         f"Valores: {x=} e {y=} | Soma: {x+y}")


# soma(1, 2)
# soma(1, 2, 3)
