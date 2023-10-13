# Modularização no Python.

import aula88modulo
# from aula88modulo import saudacao

mensagem = aula88modulo.saudacao("Valmir")
# mensagem = saudacao("Valmir")

print(mensagem)

"""
Observações:

1) O Python segue uma ordem específica ao pesquisar por módulos. Ele primeiro verifica os diretórios na lista "sys.path", na ordem em que eles aparecem. Os diretórios incluem:

- O diretório do script em execução (o diretório atual).
- Os diretórios listados na variável de ambiente "PYTHONPATH".
- Diretórios padrão do sistema, onde os módulos Python padrão estão instalados.

2) "sys.path" é uma lista que contém uma série de diretórios onde o Python procura por módulos. Quando você importa um módulo, o Python verifica cada diretório na lista em busca do módulo desejado.

3) Você pode adicionar, modificar ou remover diretórios da lista "sys.path" durante a execução do seu programa, permitindo que você influencie a pesquisa de módulos.

- Para adicionar um diretório à lista "sys.path", você pode usar "sys.path.append(diretorio)" ou "sys.path.insert(indice, diretorio)".
- Para remover um diretório da lista "sys.path", você pode usar "sys.path.remove(diretorio)".

4) Exemplo de uso:
   
   import sys

   # Exibe os diretórios em sys.path
   for diretorio in sys.path:
       print(diretorio)

   Este código imprimirá os diretórios onde o Python procura por módulos, incluindo o diretório atual, diretórios definidos na variável "PYTHONPATH" e os diretórios padrão do sistema.

5) Ambiente virtual (Virtualenv): ambientes virtuais, criados com ferramentas como "virtualenv" ou o módulo "venv" da biblioteca padrão, também afetam o "sys.path". Eles permitem isolar as dependências de um projeto específico e podem modificar o "sys.path" temporariamente para apontar para o ambiente virtual apropriado.

6) Evitando conflitos e problemas: é importante usar o "sys.path" com cuidado para evitar conflitos entre módulos de diferentes projetos. Dependendo do ambiente de desenvolvimento, você pode encontrar problemas se não gerenciar adequadamente o "sys.path".

Em resumo, "sys.path" é uma lista de diretórios usada pelo Python para encontrar módulos e pacotes. Entender como funciona o "sys.path" é fundamental para gerenciar dependências e organizar projetos Python de forma eficaz.
"""
