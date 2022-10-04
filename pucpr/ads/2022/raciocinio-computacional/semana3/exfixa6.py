# Unidade 03: Estruturas de repetição.
# Exercício de fixação 6: Crie um programa que peça para o usuário inserir um login e uma senha. Caso os valores sejam
# iguais, informar que os dados são inválidos e pedir novamente as informações. Caso contrário,
# exibir a mensagem "Bem-vindo ao sistema!".

while True:
    login = str(input('Informe o seu login: '))
    senha = str(input('Informe a sua senha: '))
    if login == senha:
        print('Dados inválidos! login e senha são iguais! Redigite as informações.')
    else:
        break
print('Bem-vindo ao sistema!')
