"""Python Brasil
Lista de exercícios de estrutura de decisão.
Exercício 25: Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"."""

print()
print('=' * 44)
print('Programa Analisador de Participação no Crime')
print('=' * 44)
print()
print('Responda as 5 perguntas a seguir e verifique se você é suspeito(a) de participar do crime')
print()
p1 = str(input('você telefonou para a vítima (S=sim/N=não)? ')).strip().upper()
p2 = str(input('você esteve no local do crime (S=sim/N=não)? ')).strip().upper()
p3 = str(input('você mora perto da vítima (S=sim/N=não)? ')).strip().upper()
p4 = str(input('você devia para a vítima (S=sim/N=não)? ')).strip().upper()
p5 = str(input('você já trabalhou com a vítima (S=sim/N=não)? ')).strip().upper()
classificacao = 0
if p1 == 'S':
    classificacao += 1
if p2 == 'S':
    classificacao += 1
if p3 == 'S':
    classificacao += 1
if p4 == 'S':
    classificacao += 1
if p5 == 'S':
    classificacao += 1
if classificacao == 2:
    print('Você é considerado "Suspeito" do crime')
elif classificacao == 3:
    print('Você é considerado "Cúmplice" do crime')
elif classificacao == 4:
    print('Você é considerado "Cúmplice" do crime')
elif classificacao == 5:
    print('Você é considerado "Assassino" do crime')
else:
    print('Você é considerado "Inocente" do crime')
