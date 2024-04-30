# Estrutura de repetição.

# for
for i in range(10):
    if i == 2:
        print("Número 2 não será impresso!")
        continue
    print(i)
    # if i == 8:
    #     print('"i" é igual a 8 e o "else" não sera executado!')
    #     break
else:
    print('"for" utilizado com sucesso!')
