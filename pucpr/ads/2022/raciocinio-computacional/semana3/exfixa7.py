# Unidade 03: Estruturas de repetição.
# Exercício de fixação 7: Crie um programa que solicite ao usuário vários números e, ao digitar 0, calcule a média dos números informados.

contador = 0
soma = 0
while True:
    num = float(input('Digite um número qualquer. Para finalizar a inserção dos valores, pressione 0: ' ))
    if num == 0:
        break
    else:
        contador += 1
        soma += num
if contador == 0:
    print('Não foi inserido nenhum número! Reinicie o processo!')
else:
    media = soma / contador
    print('A média dos {} números inseridos é: {:.2f}'.format(contador, media))
