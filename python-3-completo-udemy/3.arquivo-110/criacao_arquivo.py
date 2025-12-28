""
Manipulação de arquivos no Python.

A manipulação de arquivos no Python é uma tarefa comum em programação, pois permite que você leia, escreva e gerencie dados armazenados em arquivos. O Python oferece várias bibliotecas e métodos embutidos para trabalhar com arquivos.
"""

"""
Criação de um arquivo no Python.

Para trabalhar com um arquivo, você primeiro precisa criá-lo usando a função "open()". Esta função recebe dois argumentos: o nome do arquivo e o modo de abertura (criação, leitura, escrita, etc.).

Os modos de abertura mais comuns são:

"w" para escrita (cria um novo arquivo ou sobrescreve o arquivo existente)
"r" para leitura (padrão)
"a" para anexar (adicionar dados ao final do arquivo)
"x" para criar um novo arquivo para escrita, falhando se o arquivo já existir
"b" para abrir o arquivo em modo binário (por exemplo, "rb" para leitura binária)
"""

arquivo = open(
    "/Users/valmirfilho/Downloads/python-3-completo-udemy/aula110/arquivo.txt", "w", encoding="utf8")
arquivo.close()

# Dessa forma não há necessidade de fechar o arquivo
# with open("/Users/valmirfilho/Downloads/python-3-completo-udemy/aula110/arquivo.txt", "w") as arquivo:
#     print("Olá Mundo!")
#     print("Arquivo será fechado!")
