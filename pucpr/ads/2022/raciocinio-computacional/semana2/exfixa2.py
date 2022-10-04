# Unidade 02: Estruturas condicionais
# Exercício de fixação 2: Crie um programa que pergunte o nome do cliente para ser inserido em um cartão de crédito,
# com espaço máximo de 20 caracteres. Caso o usuário informe um nome maior, deve mostrar uma mensagem informando que
# o nome é extenso demais e deve ser abreviado. Dica: para saber o tamanho de uma string, usar a função len.
# Exemplo: len(nome).

nome = input("Digite o seu nome para ser inserido no cartão de crédito: ")
if len(nome) >= 20:
    print("O seu nome ultrapassa 20 caracteres, por favor, abrevie.")
else:
    print("O seu nome foi inserido no cartão de crédito com sucesso")
