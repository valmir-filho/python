""""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com
a tabela abaixo:
- IMC abaixo de 18.5: ABAIXO DO PESO;
- IMC entre 18.5 e 25: PESO IDEAL;
- IMC entre 25 e 30: SOBREPESO;
- IMC entre 30 e 40: OBESIDADE;
- IMC acima de 40: OBESIDADE MÓRBIDA."""

peso = float(input('Informe o seu peso (em kg): '))
altura = float(input('Informe a sua altura (em metros): '))
imc = peso / altura**2
print('O seu IMC é igual a: {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você está abaixo do peso')
elif 18.5 < imc <= 25:
    print('Você está no peso ideal')
elif 25 < imc <= 30:
    print('Você está com sobrepeso')
elif 30 < imc <= 40:
    print('Você está com obesidade')
else:
    print('Você está com obesidade mórbida')
