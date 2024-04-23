"""Python Brasil
Lista de exercícios de funcões.
Exercício 5: Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto,
que é a quantia de imposto sobre vendas, expressa em porcentagem, e custo, que é o custo de um item antes do imposto. A
função “altera” o valor de custo para incluir o imposto sobre vendas."""


def soma_imposto(taxa_imposto, custo):
    valor = custo + (custo * taxa_imposto/100)
    print(f'O valor de R${custo}, após a incidência da taxa de imposto de {taxa_imposto}%, é igual a: R${valor}.')


soma_imposto(15, 1000)
