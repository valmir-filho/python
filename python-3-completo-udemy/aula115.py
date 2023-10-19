# Exercício: criar um organizador de tarefas.

import os

lista = []

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
    elif tarefa == "REFAZER":
        if not lista:
            print("\nNão é possível refazer! Lista vazia.")
        else:
            lista.append(item_removido)
            print(f"\nTarefa {lista[-1]} adicionada a lista com sucesso!")
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
