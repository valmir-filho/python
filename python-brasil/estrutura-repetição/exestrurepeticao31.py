"""Python Brasil
Lista de exercícios de estrutura de repetição.
Exercício 31: O Sr. Manoel Joaquim expandiu os seus negócios para além dos negócios de 1,99 e agora possui uma loja de
conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número
desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para
indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o
cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto
inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 8.00
Dinheiro: R$ 20.00
Troco: R$ 12.00"""

total_compra = []
print('LOJAS TABAJARA')
while True:
    produto = float(input('Informe o valor do produto em R$. Para encerrar, digite 0: '))
    total_compra.append(produto)
    if produto == 0:
        print(f'O valor total da compra é de R${sum(total_compra):.2f}.')
        dinheiro = float(input('Informe o valor em dinheiro fornecido pelo cliente R$'))
        print(f'Valor do troco R${dinheiro-sum(total_compra):.2f}.')
        print('Obrigado por comprar nas Lojas Tabajara!!!')
        print()
