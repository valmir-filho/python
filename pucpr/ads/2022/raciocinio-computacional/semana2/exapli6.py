# Unidade 02: Estruturas condicionais
# Exemplo de aplicação 6: Elabore um programa que solicite ao usuário as notas de determinada disciplina escolar e
# calcule a média. Se a média for maior ou igual a 7, deve mostrar ao aluno que ele foi aprovado; caso contrário,
# que foi reprovado.

nota1 = float(input("Informe a nota do 1º bimestre da disciplina: "))
nota2 = float(input("Informe a nota do 2º bimestre da disciplina: "))
nota3 = float(input("Informe a nota do 3º bimestre da disciplina: "))
nota4 = float(input("Informe a nota do 4º bimestre da disciplina: "))
media = (nota1 + nota2 + nota3 + nota4)/4
print("A sua média é", media)
if media >= 7:
    print("Você está aprovado na disciplina...:)")
else:
    print("Você está reprovado na disciplina...:/")
