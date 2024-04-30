"""
Módulo __main__ no Python.

O módulo __main__ é um conceito fundamental em Python que está relacionado à forma como os programas Python são executados. O __main__ não é um módulo específico que você cria; em vez disso, é automaticamente criado pelo interpretador Python quando você executa um script Python. 

Aqui estão os principais pontos sobre o módulo __main__:

- Identificação de um programa principal: quando você executa um arquivo Python diretamente, por exemplo, usando o comando python arquivo.py, o Python cria automaticamente um namespace especial chamado __main__. O código no arquivo Python é executado no contexto deste namespace __main__.

- O módulo __main__ é frequentemente usado para criar scripts executáveis. Ou seja, você pode colocar o código que deseja executar quando o script é chamado diretamente dentro deste módulo.

- Isso é útil para distinguir entre a execução direta de um arquivo Python e a importação desse arquivo como um módulo em outro script.

- Evitando a execução não desejada: a utilização do if __name__ == "__main__": ajuda a evitar que o código dentro de um arquivo seja executado quando o arquivo é importado como um módulo em outro script. Isso é útil para evitar efeitos colaterais indesejados.

- Modularidade: o uso do módulo __main__ promove a modularidade e a reutilização de código, permitindo que você crie scripts reutilizáveis que podem ser executados como programas independentes ou importados como módulos em outros scripts.

Em resumo, o módulo __main__ é uma parte importante da estrutura de um programa Python que permite criar scripts executáveis e modularizar o código de forma eficaz. Ele ajuda a controlar o comportamento do código quando é executado diretamente ou quando é importado como um módulo em outros scripts.
"""

# Suponha que você tenha o seguinte código em um arquivo chamado "meuscript.py":


def funcao_principal():
    print("Esta é a função principal.")


if __name__ == "__main__":
    funcao_principal()

"""
Quando você executa "python meuscript.py", o código dentro do bloco if __name__ == "__main__": é executado, e a saída será "Esta é a função principal.". No entanto, se você importar "meuscript.py "em outro script, o código dentro do bloco if __name__ == "__main__": não será executado automaticamente.
"""
