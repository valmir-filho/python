# Testando as cores no terminal do Python (usando padrão ANSI).

print('\033[30mOlá mundo!')  # apenas letra cor padrão.
print('\033[31mOlá mundo!')  # apenas letra cor vermelha.
print('\033[32mOlá mundo!')  # apenas letra cor verde.
print('\033[33mOlá mundo!')  # apenas letra cor amarela.
print('\033[34mOlá mundo!')  # apenas letra cor azul.
print('\033[35mOlá mundo!')  # apenas letra cor magenta.
print('\033[36mOlá mundo!')  # apenas letra cor ciano.
print('\033[37mOlá mundo!')  # apenas letra cor cinza.
print('\033[0mOlá mundo!')  # apenas estilo da letra padrão.
print('\033[1mOlá mundo!')  # apenas estilo da letra negrito.
print('\033[4mOlá mundo!')  # apenas estilo da letra sublinhado.
print('\033[7mOlá mundo!')  # apenas estilo da letra negativo (inverte a cor do fundo com a da letra).
print('\033[;40mOlá mundo!')  # apenas fundo branco (como o meu já estava branco, ele inverte).
print('\033[;41mOlá mundo!')  # apenas fundo vermelho.
print('\033[;42mOlá mundo!')  # apenas fundo verde.
print('\033[;43mOlá mundo!')  # apenas fundo amarelo.
print('\033[;44mOlá mundo!')  # apenas fundo azul.
print('\033[;45mOlá mundo!')  # apenas fundo magenta.
print('\033[;46mOlá mundo!')  # apenas fundo ciano.
print('\033[;47mOlá mundo!')  # apenas fundo cinza.
print('\033[4;33;45mOlá mundo!')  # pode combinar (estilo, cor da letra, fundo) tudo em simultâneo, basta apenas
# colocar os códigos específicos, separados por ;.
print('\033[1;35;42mOlá mundo!\033[m')  # para deixar apenas em cima do texto o fundo, usa o comando no final do print,
# sem nenhum código.

# Outra forma de representar, usando a função .format.

nome = 'Valmir Moro'
print('Olá! Muito prazer em te conhecer, {}{}{}.'.format('\033[34m', nome, '\033[m'))
