"""Python Brasil
Lista de exercícios de estrutura de decisão.
Exercício 3: Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra, escrever: F — Feminino,
M — Masculino, Sexo Inválido."""

letra = str(input('Digita a letra "M" para sexo masculino ou "F" para sexo feminino: ')).strip().upper()
if letra == 'M':
    print('M - Masculino')
elif letra == 'F':
    print('F - Feminino')
else:
    print('Sexo Inválido!!!')
