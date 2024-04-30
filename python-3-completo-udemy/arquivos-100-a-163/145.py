"""
Gerenciador de contexto no Python.

Um gerenciador de contexto (context manager) é um recurso do Python que permite a você controlar a aquisição e a liberação de recursos, como arquivos, conexões de
banco de dados e outros objetos que requerem uma limpeza apropriada. Você pode criar gerenciadores de contexto personalizados definindo classes com métodos
especiais "__enter__" e "__exit__".
"""

import time


class MedidorDeTempo:
    def __enter__(self):
        self.inicio = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.fim = time.time()
        tempo_decorrido = self.fim - self.inicio
        print(f"Tempo decorrido: {tempo_decorrido} segundos.")


# Usando o gerenciador de contexto para medir o tempo de execução
with MedidorDeTempo():
    # Simulando uma operação demorada
    for _ in range(1000000):
        pass

# O tempo decorrido será impresso automaticamente ao sair do contexto

"""
Neste exemplo, a classe "MedidorDeTempo" é um gerenciador de contexto. Quando entramos no bloco with, o método "__enter__" é chamado, que registra o tempo de início
da operação. Quando saímos do bloco with, o método "__exit__" é chamado, que calcula o tempo decorrido e o imprime.

Ao executar o código acima, você verá o tempo decorrido da operação dentro do bloco with impresso na saída.

Esse é um exemplo simples de como criar e usar um gerenciador de contexto personalizado no Python. Você pode adaptar essa abordagem para suas necessidades
específicas, como manipular arquivos, conexões de banco de dados ou qualquer outra tarefa que requeira limpeza ou medição de tempo.
"""
