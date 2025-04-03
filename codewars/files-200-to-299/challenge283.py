"""
The Arara is an isolated tribe found in the Amazon who count in pairs. For example one to eight is as follows:

1 = anane
2 = adak
3 = adak anane
4 = adak adak
5 = adak adak anane
6 = adak adak adak
7 = adak adak adak anane
8 = adak adak adak adak

Take a given number and return the Arara's equivalent.
"""


def count_arara(n):
    pairs = n // 2
    result = ['adak'] * pairs
    if n % 2 == 1:
        result.append('anane')
    return ' '.join(result)
