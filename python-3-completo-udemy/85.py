"""
raise no Python.

No Python, a palavra-chave "raise" é usada para explicitamente levantar uma exceção. Isso permite que você indique que ocorreu uma condição excepcional em seu código e que você deseja sinalizá-la, para que possa ser tratada adequadamente em outro lugar do programa. O comando raise é útil para criar exceções personalizadas, relançar exceções capturadas ou sinalizar erros específicos.

Principais conceitos relacionados ao uso de "raise" no Python:

- Levantando exceções: o comando raise é seguido pelo nome de uma exceção ou uma instância de exceção. Por exemplo, "raise ValueError" levanta uma exceção do tipo "ValueError".

- Personalizando exceções: você pode criar suas próprias exceções personalizadas para situações específicas do seu programa.

- Relançando exceções: às vezes, você pode querer capturar uma exceção e depois relançá-la para que seja tratada em um nível superior. Você pode fazer isso simplesmente usando raise dentro de um bloco "except".

- Especificando detalhes da exceção: você pode fornecer informações adicionais sobre a exceção levantada, passando argumentos para o construtor da exceção. Isso pode ser útil para incluir mensagens de erro ou outros dados relevantes.

- Tipos embutidos de exceções: Python inclui muitos tipos de exceções embutidos para situações comuns, como "ValueError", "TypeError", "ZeroDivisionError", entre outros. Você pode levantar essas exceções embutidas ou criar suas próprias exceções personalizadas quando necessário.

O uso correto do "raise" é uma parte importante da manipulação de exceções no Python. Ele ajuda a tornar o código mais robusto e a fornecer informações úteis para depuração e tratamento de erros adequado.

Observações:

- Usar o "raise" para levantar uma exceção interrompe a execução do programa no ponto em que a exceção é lançada, a menos que a exceção seja capturada e tratada posteriormente. Isso ajuda a evitar que o programa continue funcionando de maneira incorreta após um erro.

- Levantar uma exceção é uma maneira formal de sinalizar que ocorreu um erro no código. Permite que você trate os erros de maneira adequada, seja lidando com eles diretamente ou passando-os para um nível superior de tratamento de exceções.

- O uso de exceções é mais adequado quando você precisa controlar o fluxo do programa com base em erros específicos ou quando deseja que os erros sejam capturados e tratados de maneira consistente em todo o código.
"""


def dividir(x, y):
    if y == 0:
        raise ValueError("Não é possível a divisão por zero.")
    return x / y


try:
    resultado = dividir(10, 0)
except ValueError as error:
    print(f"Erro! {error}")
else:
    print(f"Resultado da divisão: {resultado}.")
