# Unidade 05: Estrutura de dados: tuplas e dicionários
"""Exemplo de aplicação 1: Elabore um programa que solicite ao usuário o cadastro de endereços para entrega de produtos
de uma loja."""

enderecos = []
print('Cadastro de Endereços de Entrega')
while True:
    logradouro = str(input("Digite o logradouro: ")).strip()
    numero = int(input('Digite o número: '))
    bairro = str(input('Digite o bairro: ')).strip()
    cidade = str(input('Digite a cidade: ')).strip()
    estado = str(input('Digite o estado: ')).strip()
    novo_endereco = (logradouro, numero, bairro, cidade, estado)
    enderecos.append(novo_endereco)
    if str(input('Deseja cadastrar um novo endereço? (S=sim/N=não): ')).strip().upper() == 'N':
        break
print('Os endereços cadastrados são: ')
for i in range(0, len(enderecos)):
    endereco = enderecos[i]
    print('{}. {}, {}, {} - {}/{}'.format(i, endereco[0], endereco[1], endereco[2], endereco[3],endereco[4]))
