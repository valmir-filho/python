# Fatiamento de strings e função len.

"""
 0123456789
 Olá Mundo!
-10987654321

Formas de usar o fatiamento: [i:f:p] [::]
"""

palavra = "Olá Mundo!"
print(palavra[5])
print(palavra[-5])

# Fatiamento

# início [i]
print(palavra[4:])  # Não precisa indicar o fim, caso eu queira toda a string

# início e fim [i:f]

"""
Se for indicado o fim, lembrar que sempre tenho que colocar um índice a mais, pois no Python,
o último índice nunca é considerado.
"""

print(palavra[4:9])
print(palavra[0:3])
print(palavra[:3])  # É possível omitir o início
print(palavra[-6:-1])
print(palavra[-6:])  # É possível omitir o final

# passo [p]
print(palavra[0:10:1])
print(palavra[0:10:2])
print(palavra[-1:-11:-1])  # É possível inverter a string

# Função len
print(len(palavra))
