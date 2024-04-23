"""Python Brasil
Lista de exercícios de estrutura de repetição.
Exercício 33: O Departamento Estadual de Meteorologia contratou-lhe para desenvolver um programa que leia um conjunto
indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das
temperaturas."""

temperaturas = []
contador = 0
print('🌧️ DEPARTAMENTO ESTADUAL DE METEOROLOGIA 🌧️')
while True:
    temperatura = float(input('Informe a temperatura em ºC: '))
    continuar = str(input('Deseja continuar incluindo temperaturas? (S=sim/N=não): ')).strip().upper()
    temperaturas.append(temperatura)
    contador += 1
    if continuar == 'N':
        print(f'A menor temperatura informada foi: {min(temperaturas)}ºC.')
        print(f'A maior temperatura informada foi: {max(temperaturas)}ºC.')
        print(f'A média das temperaturas é de: {sum(temperaturas) / contador:.1f}ºC.')
        break
