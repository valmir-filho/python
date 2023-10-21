# Comparação entre method, @classmethod e @staticmethod

class Connection:
    def __init__(self, host="localhost"):
        self.host = host

    # Métodos de instância
    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.set_password = password

    # Método de classe
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    # Método estático
    @staticmethod
    def log_message(msg):
        print(f"Log message: {msg}")


# Para o método de instância
c1 = Connection()
c1.set_user = "vmcfilho"
c1.set_password = 123456
print(c1.set_user, c1.set_password)

# Para o método de classe
# c1 = Connection.create_with_auth("vmcfilho", 123456)
# print(c1.user, c1.password)

# Para o método estático
# print(Connection.log_message("Essa é a mensagem de log."))
