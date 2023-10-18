"""
os.remove() e os.unlink() no Python.

Ambas as funções "os.remove()" e "os.unlink()" são usadas para excluir (ou "remover" ou "desvincular") um arquivo do sistema de arquivos. Elas são sinônimos e podem ser usadas de forma intercambiável. A principal diferença entre elas é o nome, sendo "os.remove()" mais comumente usado.
"""

import os

file_path = "/Users/valmirfilho/Downloads/python-3-completo-udemy/aula111/arquivo.txt"

try:
    os.remove(file_path)  # ou os.unlink(file_path)
    print(f"O arquivo {file_path} foi removido com sucesso!")
except FileNotFoundError:
    print(f"Erro! O arquivo {file_path} não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao remover o arquivo: {e}.")
