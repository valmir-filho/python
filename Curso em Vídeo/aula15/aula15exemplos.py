# Aplicações do comando "break"" e das "fstrings" do Python.

soma = []
while True:
    n = int(input('Digite um número inteiro qualquer: '))
    soma.append(n)
    if n == 0:
        break
print(f'A soma dos número digitados é igual a: {sum(soma)}.')  # esse "f" substitui o comando ".format".

nome = 'Valmir'
sobrenome = 'Moro Conque Filho'
idade = 42
salario = 987.454
print(f'{nome} {sobrenome} tem {idade} anos e ganha R${salario:.2f}.')
