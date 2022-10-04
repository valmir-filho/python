# Unidade 06: Funções
"""Encadeamento de funções
As funções podem ter chamadas encadeadas, de qualquer lugar, inclusive de dentro do corpo de outra função. Isso
corrobora o conceito de modularizar os códigos o máximo possível, devendo uma função executar, normalmente, uma única
tarefa."""

# Exemplo de aplicação 5: Elabore um programa que, aplicando a fórmula de Bhaskara por funções, encontre as raízes de
# um polinômio do segundo grau.

def delta(a,b,c):
    return b**2 - 4*a*c
def bhaskara(a,b,c):
    d = delta(a,b,c)
    if d < 0:
        print('A equação não possui valores reais')
        return 0,0,False
    else:
        x1 = (-b+d**0.5)/2*a
        x2 = (-b-d**0.5)/2*a
        return x1,x2,True
teste1 = bhaskara(1,3,1)
if teste1[2]:
    print('As raízes são: {:.2f} e {:.2f}'.format(teste1[0], teste1[1]))
teste2 = bhaskara(1,2,1)
if teste2[2]:
    print('As raízes são: {:.2f} e {:.2f}'.format(teste2[0], teste2[1]))
teste3 = bhaskara(1,1,1)
if teste3[2]:
    print('As raízes são: {:.2f} e {:.2f}'.format(teste3[0], teste3[1]))
