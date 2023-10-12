"""
1) Peça para o usuário digitar o seu nome.
2) Peça para o usuário digitar a sua idade.
3) 
Se o nome e a idade forem digitados:
Exiba:
    - Seu nome é {nome}
    - Seu nome invertido é {nome invertido}
    - Seu nome contém (ou não) espaços
    - Seu nome tem {n} letras
    - A primeira letra do seu nome é {letra}
    - A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
Exiba:
    - "Desculpe, você deixou um dos campos vazios!
"""

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")

# A verificação do nome e da idade (se os campos estão vazios) está implícita
if nome and idade:
    print(f"Seu nome é {nome}.")
    print(f"Seu nome invertido é {nome[::-1]}.")

    """
    Possível forma a ser utilizada para inverter uma string

    print(f"Seu nome invertido é {nome[::-1]}")
    
    O primeiro : indica o início do fatiamento, que está em branco, indicando que começaremos do primeiro caractere da sequência (índice 0).
    O segundo : indica o final do fatiamento, que também está em branco, indicando que iremos até o último caractere da sequência.
    O -1 indica o passo, que é negativo. Isso significa que estamos percorrendo a sequência de trás para frente, do último caractere ao primeiro.
    """

    if " " in nome:
        print("Seu nome contém espaços.")
    else:
        print("Seu nome não contém espaços.")

    print(f"Seu nome contém {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}.")
    print(f"A última letra do seu nome é {nome[-1]}.")

else:
    print("Erro! Você deixou um dos campos vazios.")
