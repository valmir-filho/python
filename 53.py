"""
Funções no Python.

As funções em Python servem para encapsular um conjunto de instruções em um bloco de código reutilizável.
Elas são uma parte fundamental da programação em Python e desempenham vários papéis importantes, incluindo:

1. Modularização: funções permitem que você divida seu código em partes menores e mais gerenciáveis.
Isso torna o código mais organizado, fácil de entender e manter.

2. Reutilização de código: você pode definir uma função uma vez e chamá-la várias vezes em seu programa, evitando a repetição de código. Isso economiza tempo e torna o código mais eficiente.

3. Abstração: funções permitem que você abstraia a lógica de um determinado conjunto de operações.
Isso significa que você pode usar uma função sem precisar conhecer todos os detalhes de como ela funciona internamente.

4. Passagem de argumentos: funções podem aceitar argumentos, que são valores que você passa para a função quando a chama.
Esses argumentos podem ser usados dentro da função para realizar operações específicas.

5. Retorno de valores: as funções podem retornar valores, que são resultados calculados pela função.
Isso permite que você obtenha resultados de uma função e os utilize em outras partes do seu programa.

6. Organização do código: funções ajudam a organizar o código de maneira mais estruturada,
dividindo-o em blocos lógicos e nomeando esses blocos de acordo com sua função.

7. Facilidade de depuração: quando ocorrem erros em seu código, as funções facilitam a identificação
e a correção desses erros, pois você pode isolar e testar partes específicas do código.

8. Encapsulamento: funções podem encapsular variáveis locais, tornando-as inacessíveis fora da função,
a menos que você as retorne explicitamente. Isso ajuda a evitar conflitos de nomes de variáveis em diferentes partes do programa.
"""


def saudacao(nome):  # Dentro do parênteses temos o parâmetro da função
    print(f"Olá, {nome}")


saudacao("Valmir")  # Dentro do parênteses temos o argumento da função
saudacao("Pedro")
