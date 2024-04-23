# Aplicações de variáveis compostas em Python.
# Dicionários

brasil = []
estado = {}
for c in range(1, 4):
    estado['Estado'] = str(input('Digite o Estado: ')).strip().upper()
    estado['Sigla'] = str(input('Digite a Sigla: ')).strip().upper()
    brasil.append(estado.copy())  # O "copy" serve para copiar o dicionário para dentro da lista.
for e in brasil:
    print(e)
