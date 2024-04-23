# Formatação de strings com o método "format".

a = "A"
b = "B"
c = 1.1
# Impressão no terminal: a = A | b = B | c = 1.1

formato = "a = {} | b = {} | c = {:.2f}".format(a, b, c)
# formato = "a = {1} | b = {0} | c = {2:.2f}".format(a, b, c)
# formato = "a = {letraA} | b = {letraB} | c = {letraC:.2f}".format(letraA=a, letraB=b, letraC=c)
# formato = "a = {letraB} | b = {letraA} | c = {letraC:.2f}".format(letraA=a, letraB=b, letraC=c)

print(formato)
