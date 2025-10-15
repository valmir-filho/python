"""
Your car is old, it breaks easily. The shock absorbers are gone and you think it can handle about 15 more bumps before it dies totally.
Unfortunately for you, your drive is very bumpy! Given a string showing either flat road (_) or bumps (n).
If you are able to reach home safely by encountering 15 bumps or less, return Woohoo!, otherwise return Car Dead.
"""


def bumps(road):
    # Conta quantas vezes aparece 'n' na string (cada 'n' é um buraco).
    bumps_count = road.count('n')
    
    # Se o número de buracos for 15 ou menos, o carro sobrevive.
    if bumps_count <= 15:
        return "Woohoo!"
    else:
        return "Car Dead"
