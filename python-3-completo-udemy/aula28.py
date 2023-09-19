# Estrutura de repetição.

numero_linhas = 5
numero_colunas = 5

linha = 1
while linha <= numero_linhas:
    coluna = 1
    while coluna <= numero_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1
print("Fim!")
