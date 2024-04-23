"""Python Brasil
Lista de exercícios de listas.
Exercício 15: Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a
entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
— Mostre a quantidade de valores que foram lidos;
— Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
— Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
— Calcule e mostre a soma dos valores;
— Calcule e mostre a média dos valores;
— Calcule e mostre a quantidade de valores acima da média calculada;
— Calcule e mostre a quantidade de valores abaixo de sete;
— Encerre o programa com uma mensagem."""

notas = []
contador_1 = contador_2 = contador_3 = 0
while True:
    nota = float(input('Digite uma nota qualquer (-1 para sair): '))
    if nota == -1:
        break
    else:
        notas.append(nota)
        contador_1 += 1
print(f'Foram digitadas {contador_1} notas.')
print(f'As notas digitadas foram: {notas}')
print(f'As notas digitadas, na ordem inversa, foram:')
notas.reverse()
for n in notas:
    print(f'{n}')
print(f'A soma das notas é igual a: {sum(notas):.2f}.')
media_notas = sum(notas)/contador_1
print(f'A média das notas é igual a: {media_notas:.2f}.')
for n in notas:
    if n > media_notas:
        contador_2 += 1
    if n < 7:
        contador_3 += 1
print(f'{contador_2} notas estão acima da média das notas.')
print(f'{contador_3} notas estão abaixo de 7.')
print('Obrigado por utilizar o programa!')
