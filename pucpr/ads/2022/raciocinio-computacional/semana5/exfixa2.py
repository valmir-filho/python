# Unidade 05: Estrutura de dados: tuplas e dicionários
"""Exercício de fixação 2: Crie um programa que cadastre os funcionários de uma empresa e os seus dependentes.
O funcionário deve ser cadastrado com matrícula, nome e dependentes. Os dependentes devem ser inseridos dinamicamente
em uma tupla. Dica: use o operador “+=”."""

funcionarios = []
while True:
    nome = str(input('Digite o nome do funcionário: ')).strip().upper()
    matricula = int(input('Digite a matrícula do funcionário: '))
    dependentes = tuple()
    while True:
        dependente = str(input('Digite o nome do dependente (0 para sair): '))
        if dependente == "0":
            break
        dependentes += (dependente,)
    funcionario = (nome, matricula, dependentes)
    funcionarios.append(funcionario)
    if str(input('Gostaria de cadastrar mais um funcionário? (S=sim/N=não): ')).strip().upper() == "N":
        break
print(funcionarios)
