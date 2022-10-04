"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. O seu aplicativo deverá analisar
se a expressão passada está com os parênteses abertos ou fechados na ordem correta."""

pilha = []
expressao = str(input('Digite a expressão: '))
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
