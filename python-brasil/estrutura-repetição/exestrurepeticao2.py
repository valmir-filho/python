"""Python Brasil
Lista de exercícios de estrutura de repetição.
Exercício 2: Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações."""

while True:
    usuario = str(input('Digite o seu usuário: '))
    senha = str(input('Digite a sua senha: '))
    if usuario == senha:
        print('Erro! o usuário e a senha não podem ser iguais.')
    else:
        break
print('Fim!')
