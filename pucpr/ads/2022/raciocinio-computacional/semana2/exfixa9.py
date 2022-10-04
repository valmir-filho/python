# Unidade 02: Estruturas condicionais
# Exercício de fixação 9: Crie um programa que simule um caixa eletrônico. O programa deverá perguntar ao usuário
# o valor do saque e depois informar quantas notas de cada valor serão fornecidas, a saber:
# Notas disponíveis: 1, 5, 10, 50 e 100 reais.
# Valor mínimo de saque: R$ 10,00.
# Valor máximo de saque: R$ 600,00.

saque = int(input("Informe o valor do saque desejado (mínimo: R$10,00 - máximo: R$600,00): "))
resto = saque
n1 = n5 = n10 = n50 = n100 = 0
if saque < 10 or saque > 600:
    print("Saque menor que o valor mínimo ou maior que o valor máximo.")
else:
    if resto >= 100:
        sobra = resto % 100
        n100 = int((resto - sobra) / 100)
        resto = sobra
    if resto >= 50:
        sobra = resto % 50
        n50 = int((resto - sobra) / 50)
        resto = sobra
    if resto >= 10:
        sobra = resto % 10
        n10 = int((resto - sobra) / 10)
        resto = sobra
    if resto >= 5:
        sobra = resto % 5
        n5 = int((resto - sobra) / 5)
        resto = sobra
    n1 = resto
    print("Você receberá:", n100, "notas de R$100,00")
    print("Você receberá:", n50, "notas de R$50,00")
    print("Você receberá:", n10, "notas de R$10,00")
    print("Você receberá:", n5, "notas de R$5,00")
    print("Você receberá:", n1, "notas de R$1,00")
