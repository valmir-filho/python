# Operadores lógicos.

"""
and (e)

Tabela Verdade e

P (True) and Q(True) = True
P (True) and Q(False) = False
P (False) and Q(True) = False
P (False) and Q(False) = False

or (ou)

Tabela Verdade ou

P (True) and Q(True) = True
P (True) and Q(False) = True
P (False) and Q(True) = True
P (False) and Q(False) = False

not (não)

Tabela Verdade não 

P (True) -> não P = False
P (False) -> não P = True

Obs.: Valores avaliados como False, são considerados Falsy. Exemplos: 0, 0.0, "", False.
Obs.: Valores avaliados como True, são considerados Truthy.
Obs.: Existe o tipo "None" que é usado para representar um "não valor".
"""

# and
entrada = input('Digite "E" para entrar no sistema: ')
senha_usuario = input("Digite a senha para entrar no sistema: ")
senha_usuario_int = int(senha_usuario)
senha_valida = 123456

if entrada == "E" and senha_usuario_int == senha_valida:
    print("Acesso realizado com sucesso!")
else:
    print("Erro! Forma de entrada no sistema e/ou senha incorreta(s).")

# or
# entrada = input('Digite "E" para entrar no sistema: ')
# senha_usuario = input("Digite a senha para entrar no sistema: ")
# senha_usuario_int = int(senha_usuario)
# senha_valida = 123456

# if (entrada == "E" or entrada == "e") and senha_usuario_int == senha_valida:
#     print("Acesso realizado com sucesso!")
# else:
#     print("Erro! Forma de entrada no sistema e/ou senha incorreta(s).")

# not
# print(not True)
# print(not False)
# print(not 0)
