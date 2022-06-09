# Unidade 05: Estrutura de dados: tuplas e dicionários
"""Exemplo de aplicação 3: Elabore um programa que concatene tuplas."""

endereco_puc = ('Rua Imaculada Conceição', 1555, 'Prado Velho', 'Curitiba','PR')
print(id(endereco_puc))
endereco_puc += ('Brasil',)
print(endereco_puc)
print(id(endereco_puc))

"""No exemplo, é possível verificar que, embora seja usado o operador '+=', pela análise dos endereços de memória, foi 
criada uma tupla, atribuída à variável endereco_puc. Outro ponto a destacar está na linha 03, em que se pode ver que
uma tupla com um único dado deve ser declarada com uma vírgula no fim; caso contrário, não será considerada uma tupla."""
