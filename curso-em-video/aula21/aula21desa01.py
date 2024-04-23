"""Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições."""


def voto(ano):
    """
    Função para verificar se o voto é obrigatório, opcional ou negado.
    :param ano: parâmetro utilizado para informar o ano de nascimento.
    :return: se a idade for menor que 16 anos, não vota. Se a idade
    estiver entre 16 e 17 ou maior que 70, o voto é opcional. Por fim,
    se a idade estiver entre 18 e 70, o voto é obrigatório.
    """
    from datetime import date
    idade = date.today().year - ano
    if 18 <= idade <= 70:
        return 'Voto obrigatório!'
    elif 16 <= idade <= 17 or idade > 70:
        return 'Voto opcional!'
    else:
        return 'Voto negado!'


nascimento = int(input('Digite o seu ano de nascimento: '))
print(voto(nascimento))
print()
help(voto)
