"""Python Brasil
Lista de exercícios de estrutura de repetição.
Exercício 3: Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd'."""

while True:
    nome = str(input('Digite o seu nome: ')).strip()
    if len(nome) < 3:
        print('Informação inválida! Digite um nome com pelo menos 3 caracteres.')
    else:
        break
while True:
    idade = int(input('Digite a sua idade: '))
    if idade < 0 or idade > 150:
        print('Informação inválida! Digite uma idade entre 0 e 150.')
    else:
        break
while True:
    salario = float(input('Digite o seu salário R$'))
    if salario <= 0:
        print('Informação inválida! Digite um salário maior que 0')
    else:
        break
while True:
    sexo = str(input('Digite o seu sexo: ')).strip().upper()
    if sexo == 'M' or sexo == 'F':
        break
    else:
        print('Informação inválida! Digite: [M]asculino/[F]eminino.')
while True:
    estado_civil = str(input('Digite o seu estado civil: ')).strip().upper()
    if estado_civil == 'S' or estado_civil == 'C' or estado_civil == 'V' or estado_civil == 'D':
        break
    else:
        print('Informação inválida! Digite: [S]olteiro(a)/[C]asado(a)/[V]iúvo(a)/[D]ivorciado(a).')
