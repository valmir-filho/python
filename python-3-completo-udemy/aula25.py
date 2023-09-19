# Estrutura de repetição.

# while
while True:
    nome = input('Digite o seu nome (Para sair, digite "Pare"): ')
    if nome.upper() == "PARE":
        break
    else:
        print(f'O seu nome é {nome}.')
