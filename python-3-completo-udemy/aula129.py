"""
Relação entre classes no Python.

No Python, assim como em muitas outras linguagens de programação orientada a objetos, você pode estabelecer relações entre classes usando três conceitos principais: associação, agregação e composição. Essas relações descrevem como as classes estão interconectadas e como uma classe pode ser usada por outra. Vamos explorar cada uma delas:

Associação:

- A associação é a relação mais simples entre classes.
- Ela ocorre quando uma classe está relacionada a outra, mas não existe uma dependência forte entre elas.
- As classes associadas podem existir independentemente uma da outra.
- A associação é geralmente implementada por meio de atributos de classe, onde uma classe contém uma referência a outra classe.

Agregação:

- A agregação é uma relação um pouco mais forte do que a associação.
- Nesse caso, uma classe é composta por outras classes, mas as classes agregadas ainda podem existir de forma independente.
- A classe que contém outras classes é chamada de classe contêiner, e as classes contidas são chamadas de classes agregadas.

Composição:

- A composição é a relação mais forte entre classes.
- Nesse caso, uma classe é composta por outras classes, e as classes compostas não fazem sentido sem a classe contêiner.
- A composição é uma forma de relação "todo-parte", onde a parte não pode existir sem o todo.

No Python, você não precisa declarar explicitamente o tipo de relação (associação, agregação ou composição) entre classes, como em algumas outras linguagens.
Em vez disso, essas relações são geralmente implementadas por meio da estrutura do código e da forma como as classes são projetadas. A compreensão desses conceitos
ajuda a modelar relacionamentos entre objetos de forma mais clara e eficiente em seus programas orientados a objetos.
"""

# Exemplo de associação


class Professor:
    def __init__(self, nome):
        self.nome = nome


class Aluno:
    def __init__(self, nome):
        self.nome = nome


class Disciplina:
    def __init__(self, nome, professor, alunos):
        self.nome = nome
        self.professor = professor
        self.alunos = alunos


prof = Professor("Dr. Smith")
aluno1 = Aluno("Alice")
aluno2 = Aluno("Bob")
disciplina = Disciplina("Matemática", prof, [aluno1, aluno2])

# Exemplo de agregação


class Carro:
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = motor


class Motor:
    def __init__(self, tipo):
        self.tipo = tipo


motor_do_carro = Motor("Elétrico")
meu_carro = Carro("Tesla", motor_do_carro)

# Exemplo de composição


class Coracao:
    def __init__(self):
        self.batendo = False


class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.coracao = Coracao()


pessoa = Pessoa("Alice")

"""
Neste exemplo de composição, a classe Pessoa é composta pela classe Coracao. A pessoa não pode existir sem um coração, e o coração não faz sentido por si só,
então é uma relação de composição.
"""