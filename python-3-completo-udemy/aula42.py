# Introdução ao desempacotamento.

lista_nomes = ["Maria", "José", "Pedro", "Ana", "Paula"]
nome1, nome2, nome3, nome4, nome5 = lista_nomes
nome1, nome2, nome3, nome4, nome5 = ["Maria", "José", "Pedro", "Ana", "Paula"]
print(nome4)
# nome1, nome2, nome3, nome4 = ["Maria", "José", "Pedro", "Ana", "Paula"]
# nome1, nome2, nome3, nome4 = ["Maria", "José", "Pedro"]
# nome1, nome2, *resto = ["Maria", "José", "Pedro", "Ana", "Paula"]  # Por convenção não fazemos dessa forma.
# Por convenção fazemos dessa forma e ignoraríamos o "underline"
# nome1, nome2, *_ = ["Maria", "José", "Pedro", "Ana", "Paula"]
# É possível imprimir a variável, mas não é recomendado.
# print(nome1, nome2, _)
# Nesse caso, ignoramos o nome1, usamos o nome2 e juntamos os demais nomes com o "*"
# _, nome2, *_ = ["Maria", "José", "Pedro", "Ana", "Paula"]
# print(nome2)
