""""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
— A média de idade do grupo;
— Qual é o nome do homem mais velho;
— Quantas mulheres tem menos de 20 anos."""

idades = []
maior_idade_homem = 0
homem_mais_velho = ''
mulheres = 0
for pessoas in range(1,5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(pessoas))).strip().upper()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(pessoas)))
    idades.append(idade)
    sexo = str(input('Digite o sexo (M=masc./F=fem.) da {}ª pessoa: '.format(pessoas))).strip().upper()
    if pessoas == 1 and sexo == 'M':
        maior_idade_homem = idade
        homem_mais_velho = nome
    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        homem_mais_velho = nome
    if sexo == 'F' and idade < 20:
        mulheres += 1
print('A média de idade do grupo é de: {:.1f} anos.'.format(sum(idades)/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, homem_mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheres))
