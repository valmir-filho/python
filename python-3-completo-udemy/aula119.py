# Métodos em classes no Python.

class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    # Método
    def acelerar(self):
        print(f"O carro {self.modelo} está acelerando.")


# Instanciando os objetos
carro1 = Carro("Volkswagen", "Fox", 2019, "Branco")
carro2 = Carro("Volkswagen", "Nivus", 2019, "Cinza")

print(carro1.marca, carro1.modelo, carro1.ano, carro1.cor)
print(carro2.marca, carro2.modelo, carro2.ano, carro2.cor)

# Chamando o método
carro1.acelerar()
carro2.acelerar()
