# Unidade 05: Estrutura de dados: tuplas e dicionários
frutas = {}
cont = 0
while cont < 5:
    cont = cont + 1
    tipo_fruta = str(input('Digite o tipo da fruta a ser cadastrada: ')).strip()
    opcao = str(input('A fruta é vendida por unidade ou kg? (Digite: u=unidade/k=kg)' )).strip().lower()
    tipo = ""
    if opcao == 'u':
        tipo = 'Unidade'
    else:
        tipo = 'kg'
    preco = float(input('Informe o valor da fruta R$:'))
    dados = [tipo_fruta, tipo, preco]
    cod = 'cod' + str(cont)
    frutas[cod] = dados
print('Unidade:')
for key, lista_fruta in frutas.items():
    if lista_fruta[1] == 'Unidade':
        print(key, lista_fruta)
print('Quilograma:')
for key, lista_fruta in frutas.items():
    if lista_fruta[1] == 'kg':
        print(key, lista_fruta)
