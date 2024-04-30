"""
Closure no Python.

Um fechamento (closure) em Python é uma função que "lembra" o ambiente no qual foi criada, mesmo depois de a função ter terminado de ser executada. Isso significa que a função pode acessar e fazer referência a variáveis e objetos do escopo onde ela foi definida, mesmo quando essa função é chamada em um escopo diferente.
"""

# Imagine que você deseja criar uma função que gere outras funções para calcular o aumento salarial de um funcionário com base em uma taxa de aumento específica. Você pode usar um closure para fazer isso.


# Esta é uma função externa que cria uma função interna (closure)
def calculo_aumento_salarial(taxa):
    # Esta é uma função interna (closure) que calcula o aumento
    def aumento_salarial(salario):
        return salario * (1 + taxa)
    return aumento_salarial  # Retorna a função interna (closure)


# Cálculo para um aumento de 10%
aumento_10_porcento = calculo_aumento_salarial(0.10)

# Cálculo para um aumento de 5%
aumento_5_porcento = calculo_aumento_salarial(0.05)

salario_inicial = 1000
salario_aumento_10_porcento = aumento_10_porcento(salario_inicial)
salario_aumento_5_porcento = aumento_5_porcento(salario_inicial)

print(salario_aumento_10_porcento)
print(salario_aumento_5_porcento)
