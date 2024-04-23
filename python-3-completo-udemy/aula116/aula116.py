# Exercício: criar um organizador de tarefas, que salve-as em um arquivo JSON.

import json
import os


def salvar_lista(lista):
    with open("/Users/valmirfilho/Downloads/python-3-completo-udemy/aula116/lista_tarefas.json", "w") as arquivo:
        json.dump(lista, arquivo)


def carregar_lista():
    try:
        with open("/Users/valmirfilho/Downloads/python-3-completo-udemy/aula116/lista_tarefas.json", "r") as arquivo:
            lista = json.load(arquivo)
        return lista
    except FileNotFoundError:
        return []


lista = carregar_lista()

print("∞∞∞ Organizador de Tarefas ∞∞∞")

while True:
    print("\nComandos permitidos:")
    print("\nListar")
    print("Desfazer")
    print("Refazer")
    print("Limpar")
    print("Sair")

    tarefa = input("\nDigite uma tarefa ou um comando: ").strip().upper()

    if tarefa not in "LISTARDESFAZERREFAZERLIMPARSAIR":
        lista.append(tarefa)
        salvar_lista(lista)
        print(f"\nTarefa {lista[-1]} adicionada a lista com sucesso!")
    elif tarefa == "LISTAR":
        if not lista:
            print("\nNão é possível listar! Lista vazia.")
        else:
            print(f"\nTarefas: {lista}.")
    elif tarefa == "DESFAZER":
        if not lista:
            print("\nNão é possível desfazer! Lista vazia.")
        else:
            print(f"\nTarefa {lista[-1]} removida da lista com sucesso!")
            item_removido = lista.pop()
            salvar_lista(lista)
    elif tarefa == "REFAZER":
        if not lista:
            print("\nNão é possível refazer! Lista vazia.")
        else:
            lista.append(item_removido)
            print(f"\nTarefa {lista[-1]} adicionada a lista com sucesso!")
            salvar_lista(lista)
    elif tarefa == "LIMPAR":
        sistema_operacional = os.name
        if sistema_operacional == "posix":  # Unix/Linux
            os.system("clear")
        elif sistema_operacional == "nt":  # Windows
            os.system("cls")
        else:
            print("Erro! Sistema operacional não suportado para limpeza do terminal.")
    elif tarefa == "SAIR":
        break

print("\nObrigado por utilizar o programa! 😉")
