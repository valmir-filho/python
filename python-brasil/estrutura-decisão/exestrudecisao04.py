"""Python Brasil
Lista de exercícios de estrutura de decisão.
Exercício 4: Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""

letra = str(input('Digite uma letra qualquer: ')).strip()
if letra == 'A':
    print('{} é uma vogal'.format(letra))
elif letra == 'E':
    print('{} é uma vogal'.format(letra))
elif letra == 'I':
    print('{} é uma vogal'.format(letra))
elif letra == 'O':
    print('{} é uma vogal'.format(letra))
elif letra == 'U':
    print('{} é uma vogal'.format(letra))
else:
    print('{} é uma consoante'.format(letra))
