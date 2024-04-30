"""
Exercício: implemente um algoritmo em Python para manipular o sistema de cadastro de um aluno.

Especificações:

1) Utilize uma lista para adicionar os dados dos alunos(nome, sobrenome e e-mail);
2) Crie um dicionário para armazenar os dados de cada aluno associado a uma chave (matrícula);
3) Cadastre cinco alunos no sistema;
4) Imprima os dados de todos dos alunos e sua matrícula.
"""

alunos = []

for _ in range(5):
    aluno = {}
    matricula = input("Digite a matrícula do aluno: ")
    nome = input("Digite o nome do aluno: ")
    sobrenome = input("Digite o sobrenome do aluno: ")
    email = input("Digite o e-mail do aluno: ")

    aluno["matricula"] = matricula
    aluno["nome"] = nome
    aluno["sobrenome"] = sobrenome
    aluno["email"] = email

    # Adicionando o dicionário a lista de alunos
    alunos.append(aluno)

print("∞∞∞ Lista de Alunos ∞∞∞")
for indice, aluno in enumerate(alunos, start=1):
    print(f"Aluno {indice}")
    for chave, valor in aluno.items():
        print(f"{chave}: {valor}")
    print()
