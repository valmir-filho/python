# Argumentos nomeados e não nomeados em funções no Python.

def soma(x, y, z):
    print(f"{x=}, {y=} e {z=} | x + y + z = {x + y + z}")
    # print(f"x={x}, y={y} e z={z} | x + y + z = {x + y + z}")


soma(1, 2, 3)  # Argumento não nomeado ou posicionais
soma(2, 1, 4)  # Tomar cuidado com a ordem
soma(y=2, x=1, z=3)  # Argumento nomeado

# Recomendação: não usar argumentos não nomeados e argumentos nomeados na mesma função
soma(2, 3, z=4)

# Nomeado um argumento, os próximos obrigatoriamente precisam ser nomeados
soma(2, y=3, z=5)
