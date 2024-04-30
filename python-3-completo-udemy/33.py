paragrafo = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."

qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

i = 0

while i < len(paragrafo):
    letra_atual = paragrafo[i]

    if letra_atual == " ":  # Para ignorar os espaços do parágrafo
        i += 1
        continue
    qtd_apareceu_mais_vezes_atual = paragrafo.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual
    i += 1

print(f'Letra que apareceu mais vezes: "{letra_apareceu_mais_vezes}".
      Total: {qtd_apareceu_mais_vezes} vezes.')
