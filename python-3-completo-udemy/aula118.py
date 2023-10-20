# Classes no Python.

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


pessoa1 = Pessoa("Valmir", "Moro")
print(pessoa1.nome, pessoa1.sobrenome)

"""
Esta é uma classe chamada "Pessoa" que possui um construtor "__init__" e dois atributos: "nome" e "sobrenome".

- class Pessoa: esta linha define a classe "Pessoa". As classes no Python são definidas usando a palavra-chave "class", seguida pelo nome da classe. No seu caso, a classe se chama "Pessoa".

- def __init__(self, nome, sobrenome): aqui, você está definindo o método construtor especial "__init__". O construtor é chamado quando um objeto da classe é criado. Ele inicializa os atributos da classe. O parâmetro "self" é uma convenção no Python que representa a própria instância da classe. Os parâmetros "nome" e "sobrenome" são passados para o construtor quando você cria um objeto.

- self.nome = nome e self.sobrenome = sobrenome: dentro do construtor, essas linhas atribuem os valores dos parâmetros "nome" e "sobrenome" aos atributos da classe "self.nome" e "self.sobrenome". Isso significa que cada objeto da classe "Pessoa" terá um "nome" e um "sobrenome" que podem ser acessados após a criação do objeto.

Agora, vamos criar um objeto da classe "Pessoa" e explicar a última parte do seu código: pessoa1 = Pessoa("Valmir", "Moro")

Nesta linha, você está criando um objeto da classe "Pessoa" chamado "pessoa1". Você está passando os valores "Valmir" e "Moro" como argumentos para o construtor. Isso significa que o "nome" de "pessoa1" será "Valmir" e o "sobrenome" será "Moro".

Por fim, você imprime os valores dos atributos "nome" e "sobrenome" do objeto "pessoa1": print(pessoa1.nome, pessoa1.sobrenome)

Isso imprimirá "Valmir Moro" no console, porque "pessoa1.nome" é igual a "Valmir" e "pessoa1.sobrenome" é igual a "Moro".

Em resumo, a classe "Pessoa" permite criar objetos que representam pessoas, com um nome e um sobrenome. Você pode criar várias instâncias dessa classe para representar diferentes pessoas com diferentes nomes e sobrenomes.
"""
