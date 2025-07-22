"""
Complete the function, which calculates how much you need to tip based on the total amount of the bill and the service.

You need to consider the following ratings:

Terrible: tip 0%
Poor: tip 5%
Good: tip 10%
Great: tip 15%
Excellent: tip 20%

The rating is case insensitive (so "great" = "GREAT").

If an unrecognised rating is received, then you need to return:

"Rating not recognised" in Javascript, Python and Ruby...
...or null in Java
...or -1 in C#

Because you're a nice person, you always round up the tip, regardless of the service.
"""

import math


def calculate_tip(amount, rating):
    # Converte a classificação para minúsculas para garantir que não diferencia maiúsculas de minúsculas.
    rating_lower = rating.lower()

    # Define as porcentagens de gorjeta.
    tip_percentages = {
        "terrible": 0.00,  # 0%.
        "poor": 0.05,    # 5%.
        "good": 0.10,    # 10%.
        "great": 0.15,   # 15%.
        "excellent": 0.20  # 20%.
    }

    # Verifica se a classificação é reconhecida.
    if rating_lower in tip_percentages:
        percentage = tip_percentages[rating_lower]
        # Calcula a gorjeta bruta.
        raw_tip = amount * percentage
        # Arredonda a gorjeta para cima usando math.ceil().
        # Converte para int, pois a gorjeta deve ser um número inteiro (arredondado para cima).
        return math.ceil(raw_tip)
    else:
        # Retorna a mensagem para classificações não reconhecidas.
        return "Rating not recognised"
    
