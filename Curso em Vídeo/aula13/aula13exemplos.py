# Exemplos com a estrutura de repetição for.

for c in range(0, 7):  # O comando for sempre ignora o último número.
    print(c)
print()
for c in range(6, 0, -1):  # Coloco o -1 para fazer em ordem decrescente.
    print(c)
print()
n = int(input('Digite um número inteiro: '))
for c in range(1, n + 1):  # a estrutura n+1 é para imprimir até o número inteiro digitado.
    print(c)
print()
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f + 1, p):
    print(c)
print()
s = 0
for c in range(0, 5):
    n = int(input('Digite um número: '))
    s += n  # É a mesma coisa que: s = s + 1
print('A soma de todos os valores digitados é: {}.'.format(s))
