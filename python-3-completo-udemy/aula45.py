# Faça uma lista de compras, onde o usuário pode inserir, apagar e listar as informações.

print("***** LISTA DE COMPRAS *****")

lista_compras = []

while True:
    
    print("\nOpções:")
    print("I - Inserir item")
    print("L - Listar item(ns)")
    print("A - Apagar item")
    print("S - Sair")
    
    entrada = input("Escolha uma opção: ").strip().upper()
    
    if entrada == "S":
        break
    elif entrada == "I":
        item_adicionado = input(
            "Digite o item a ser inserido na lista: ").strip().capitalize()
        lista_compras.append(item_adicionado)
        print(f"{item_adicionado} adicionado à lista de compras com sucesso.")
    elif entrada == "L":
        if not lista_compras:
            print("Erro! Lista de compras vazia.")
        else:
            print("Lista de compras atual:")
            for item in lista_compras:
                print(item)
    elif entrada == "A":
        if not lista_compras:
            print("Erro! Lista de compras vazia.")
        else:
            item_excluido = input(
                "Qual item da lista você deseja excluir? ").strip().capitalize()
            if item_excluido in lista_compras:
                lista_compras.remove(item_excluido)
                print(f"{item_excluido} removido da lista de compras com sucesso.")
            else:
                print("Erro! Item não encontrado na lista de compras.")
    else:
        print("Opção inválida! Tente novamente.")

print("Obrigado por utilizar o programa!")
