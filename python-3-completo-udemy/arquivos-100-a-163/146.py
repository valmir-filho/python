"""
Exceptions em context manager com classes no Python.

Neste exemplo, vamos criar um gerenciador de contexto que lida com exceções e faz o rollback de uma transação em um banco de dados fictício, caso ocorra uma exceção.
Vamos usar uma classe chamada "GerenciadorBancoDeDados".
"""


class GerenciadorBancoDeDados:
    def __init__(self):
        # Simula a inicialização de uma conexão com o banco de dados
        self.conexao_aberta = False

    def __enter__(self):
        # Simula a abertura da transação do banco de dados
        self.iniciar_transacao()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            # Se nenhuma exceção ocorreu, podemos confirmar a transação
            self.confirmar_transacao()
        else:
            # Se uma exceção ocorreu, faremos rollback
            self.rollback_transacao()
        
        # Simula o fechamento da conexão com o banco de dados
        self.fechar_conexao()

    def iniciar_transacao(self):
        print("Iniciando transação no banco de dados.")
        self.conexao_aberta = True

    def confirmar_transacao(self):
        print("Confirmando transação no banco de dados.")

    def rollback_transacao(self):
        print("Rollback da transação no banco de dados.")

    def fechar_conexao(self):
        print("Fechando a conexão com o banco de dados.")
        self.conexao_aberta = False


# Usando o gerenciador de contexto para interagir com o banco de dados
with GerenciadorBancoDeDados():
    # Simula uma operação bem-sucedida
    print("Operação bem-sucedida.")

# Em caso de exceção, o gerenciador de contexto garantirá o rollback da transação
with GerenciadorBancoDeDados():
    # Simula uma operação que gera uma exceção
    print("Operação que gera exceção.")
    raise ValueError("Erro simulado.")

# Após sair do contexto, o gerenciador de contexto garante que a conexão seja fechada

"""
Neste exemplo, o gerenciador de contexto "GerenciadorBancoDeDados" controla as operações no banco de dados. Quando não ocorrem exceções, a transação é confirmada no
método "__exit__", e a conexão é fechada. No entanto, se uma exceção ocorre, o método "__exit__" executa o rollback da transação para garantir a consistência dos
dados no banco de dados.
"""
