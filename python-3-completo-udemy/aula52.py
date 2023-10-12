"""
Exercício: validador de CPF

As regras da Receita Federal do Brasil para validar um CPF são baseadas no algoritmo conhecido como "Módulo 11". 

O CPF é um número de 11 dígitos, e os dois últimos são os dígitos verificadores, usados para garantir a integridade do número.

Abaixo estão as regras para validar um CPF:

1) Tamanho: O CPF deve ter exatamente 11 dígitos.

2) Dígitos iguais: Todos os dígitos não podem ser iguais. Por exemplo: "111.111.111-11" não é um CPF válido.

3) Cálculo do 1º dígito verificador:

- Multiplica-se os nove primeiros dígitos pelas potências de 10: de 10 a 2.
- Soma-se os resultados das multiplicações.
- O primeiro dígito verificador é o resultado da seguinte operação: 11 menos o resto da divisão da soma por 11.
- Se o resultado for 10 ou 11, o dígito verificador é zero.

4) Cálculo do 2º dígito verificador:

- Multiplica-se os dez primeiros dígitos pelas potências de 11: de 11 a 2.
- Soma-se os resultados das multiplicações.
- O segundo dígito verificador é o resultado da seguinte operação: 11 menos o resto da divisão da soma por 11.
- Se o resultado for 10 ou 11, o dígito verificador é zero.

5) Comparação com os dígitos verificadores originais:

- Os dois dígitos verificadores calculados são comparados com os dois últimos dígitos do CPF.
- Se ambos os dígitos verificadores calculados forem iguais aos dígitos originais, o CPF é válido. Caso contrário, o CPF é considerado inválido.

Observação: usar o site: https://www.4devs.com.br/validador_cpf para gerar CPF válidos e testar o algoritmo.
"""

print("***** VALIDADOR DE CPF *****")
print("Obs.: Digite apenas os números!")

while True:
    cpf = input("Digite o CPF para validação (ou ENTER para sair): ").strip()
    
    # Verifica se o usuário pressionou Enter para sair
    if cpf == "":
        break
    
    # Verifica se a entrada contém apenas numeros
    if not cpf.isdigit():
        print("Erro! Digite apenas números.")
        continue
    
    # Verifica se o CPF contém 11 dígitos
    if len(cpf) != 11:
        print("Erro! número de dígitos incorreto.")
    else:
        
        # Verifica se todos os dígitos são iguais. Se sim, o CPF é inválido
        if cpf == cpf[0] * 11:
            print("Erro! CPF inválido (todos os dígitos são iguais).")
        else:
            # Cálculo do primeiro dígito verificador
            soma = 0
            for i in range(9):
                soma += int(cpf[i]) * (10 - i)
            resto = 11 - (soma % 11)
            if resto == 10 or resto == 11:
                resto = 0
            if resto != int(cpf[9]):
                print(
                    f" O CPF {cpf} é inválido! O 1º dígito verificador está incorreto.")
            else:
                # Cálculo do segundo dígito verificador
                soma = 0
                for i in range(10):
                    soma += int(cpf[i]) * (11 - i)
                resto = 11 - (soma % 11)
                if resto == 10 or resto == 11:
                    resto = 0
                if resto != int(cpf[10]):
                    print(
                        f" O CPF {cpf} é inválido! O 2º dígito verificador está incorreto.")
                else:
                    print(
                        f"O CPF {cpf} é válido de acordo com as regras da Receita Federal do Brasil.")

print("Obrigado por utilizar o programa!")
