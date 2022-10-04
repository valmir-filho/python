# Unidade 05: Estrutura de dados: tuplas e dicionários
"""Um dicionário é um objeto em Python, ou seja, não faz parte dos tipos primitivos. Assim, possui métodos, que são
ações que podem ser realizadas."""

agenda = {'Maria': '(41)98765-4321', 'João': '(11)12345-6789', 'Rosana': '(21)91827-3645'}
print(agenda)
print()
# Adiciona um novo elemento no vetor.
agenda['José'] = '(19)98877-1122'
print(agenda)
print()
# Cria um dicionário com chaves e valores específicos.
chaves = ['chave1', 'chave2', 'chave3']
valores = 'teste'
novo_dicionario = dict.fromkeys(chaves, valores)
print(novo_dicionario)
print()
# Mostra a lista de itens do dicionário.
print(agenda.items())
print()
# Mostra a lista de chaves do dicionário.
print(agenda.keys())
print()
# Mostra a lista de valores do dicionário.
print(agenda.values())
print()
# Remove um item de chave específica.
agenda.pop('Maria')
print(agenda)
print()
# Remove o último item inserido (nesse caso, foi o José).
agenda.popitem()
print(agenda)
print()
# Retorna ou insere o valor de uma chave em específico.
print(agenda.setdefault('Rosana', '(21)91827-3645'))
print(agenda.setdefault('Maria', '(41)98765-4321'))
print(agenda)
print()
# Adiciona o conteúdo de um dicionário a outro.
agenda.update(novo_dicionario)
print(agenda)
print()
# Limpa o conteúdo de um dicionário.
agenda.clear()
print(agenda)
