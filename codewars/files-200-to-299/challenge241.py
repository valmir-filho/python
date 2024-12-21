"""
There's a "3 for 2" (or "2+1" if you like) offer on mangoes.
For a given quantity and price (per mango), calculate the total cost of the mangoes.
"""


def mango(quantity, price):
    # Calculate the number of mangoes you pay for.
    chargeable_mangoes = (quantity // 3) * 2 + (quantity % 3)
    # Calculate the total cost.
    total_cost = chargeable_mangoes * price
    return total_cost
