# yeld from no Python.

def gerador1():
    yield "A"
    yield "B"


def gerador2(gerador1):
    yield from gerador1()
    yield "C"
    yield "D"


resultado = gerador2(gerador1)

print(next(resultado))
# print(next(resultado))
# print(next(resultado))
# print(next(resultado))
# print(next(resultado))
