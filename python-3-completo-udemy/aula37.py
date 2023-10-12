"""
Faça um jogo para o usuário advinhar qual a palavra secreta.
Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra. Após isso, você vai conferir se a letra digitada existe na palavra. Se a letra existir, exiba a letra na posição correta da palavra. Se não, exiba um asterisco. Faça a contagem do número de tentativas utilizadas pelo usuário.
"""

import random

# Lista de palavras secretas
palavras_secretas = ["python", "programacao",
                     "computador", "inteligencia", "aprendizado"]

# Escolha aleatória da palavra secreta
palavra_secreta = random.choice(palavras_secretas)

# Inicialização das variáveis
tentativas = 0
palavra_descoberta = ["*"] * len(palavra_secreta)

print("Bem-vindo ao Jogo da Advinhação!")
print("Adivinhe a palavra secreta digitando uma letra de cada vez.")
print(f"A palavra secreta tem {len(palavra_secreta)} letras.")
print(" ".join(palavra_descoberta))

# Loop principal do jogo
while True:
    letra = input("Digite uma letra: ").lower()
    
    # Verifica se o input é valido (se não é número ou maius de uma única letra)
    if len(letra) != 1 or not letra.isalpha():
        print("Erro! Caracter inválido.")
        continue
    tentativas += 1
    
    # Verifica se a letra está na palavra secreta
    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                palavra_descoberta[i] = letra
        print(" ".join(palavra_descoberta))
        
        # Verifica se o usuário descobriu a palavra completa
        if "".join(palavra_descoberta) == palavra_secreta:
            print(
                f"Parabéns! Você adivinhou a palavra secreta: {palavra_secreta}.")
            print(f"Número de tentativas: {tentativas}.")
            break
    else:
        print("Errou! Essa letra não existe na palavra secreta.")

print("Fim de jogo! Obrigado por participar.")
