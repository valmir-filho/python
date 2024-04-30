"""
Levantando e tratando as próprias exceções no Python.

No Python, você pode levantar e tratar suas próprias exceções usando o mecanismo de exceções embutido na linguagem. Isso permite que você lide com erros e situações
excepcionais de maneira mais controlada e robusta. Para levantar uma exceção personalizada, você pode criar uma classe de exceção personalizada que herda da classe
base "Exception" ou de alguma outra classe de exceção, dependendo do seu caso.
"""


class MinhaExcecaoPersonalizada(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


# Função que pode levantar a exceção
def minha_funcao():
    # Condição para levantar a exceção
    if alguma_condicao:
        raise MinhaExcecaoPersonalizada("Ocorreu um erro específico nesta função.")


# Tratar a exceção
try:
    minha_funcao()
except MinhaExcecaoPersonalizada as e:
    print(f"Exceção capturada: {e}.")
else:
    print("Nenhuma exceção ocorreu.")

""""
Neste exemplo:

- Definimos uma classe de exceção personalizada chamada "MinhaExcecaoPersonalizada" que herda da classe base "Exception". Você pode personalizar essa classe de
exceção de acordo com suas necessidades.

- Na função "minha_funcao()", verificamos alguma condição e, se essa condição for verdadeira, levantamos a exceção personalizada usando a instrução "raise".

- Em seguida, usamos um bloco "try" e "except" para tratar a exceção. Se a exceção "MinhaExcecaoPersonalizada" for levantada, ela será capturada e o código no bloco
"except" será executado, imprimindo uma mensagem de erro.

Você pode personalizar ainda mais o tratamento da exceção de acordo com suas necessidades, incluindo a capacidade de registrar informações adicionais ou executar
ações específicas ao capturar a exceção. Isso ajuda a tornar o código mais robusto e a lidar melhor com situações excepcionais.
"""
