"""
os.rename() no Python.

A função "os.rename()" é usada para renomear um arquivo ou mover um arquivo de um local para outro. Ela aceita dois argumentos: o nome atual do arquivo e o novo nome do arquivo (ou o caminho de destino, se você estiver movendo o arquivo).
"""

import os

# Exemplo para renomear um arquivo
old_file_name = "/Users/valmirfilho/Downloads/python-3-completo-udemy/aula112/arquivo.txt"
new_file_name = "/Users/valmirfilho/Downloads/python-3-completo-udemy/aula112/arquivo_renomeado.txt"

try:
    os.rename(old_file_name, new_file_name)
    print(f"O arquivo {old_file_name} foi renomeado para {new_file_name}.")
except FileNotFoundError:
    print(f"Erro! O arquivo {old_file_name} não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao renomear o arquivo: {e}.")

# Exemplo para mover um arquivo
# import os

# source_path = "arquivo.txt"
# destination_path = "pasta_destino/arquivo.txt"

# try:
#     os.rename(source_path, destination_path)
#     print(f"O arquivo foi movido de {source_path} para {destination_path}.")
# except FileNotFoundError:
#     print(f"Erro! O arquivo {source_path} não foi encontrado.")
# except Exception as e:
#     print(f"Ocorreu um erro ao mover o arquivo: {e}.")
