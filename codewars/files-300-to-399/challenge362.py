"""
My friend John likes to go to the cinema. He can choose between system A and system B.

System A : he buys a ticket (15 dollars) every time
System B : he buys a card (500 dollars) and a first ticket for 0.90 times the ticket price, then for each additional ticket he pays 0.90 times the price paid for the previous ticket.

Example: If John goes to the cinema 3 times:

System A : 15 * 3 = 45
System B : 500 + 15 * 0.90 + (15 * 0.90) * 0.90 + (15 * 0.90 * 0.90) * 0.90 ( = 536.5849999999999, no rounding for each ticket)

John wants to know how many times he must go to the cinema so that the final result of System B, when rounded up to the next dollar, will be cheaper than System A.

The function movie has 3 parameters: card (price of the card), ticket (normal price of a ticket),
perc (fraction of what he paid for the previous ticket) and returns the first n such that ceil(price of System B) < price of System A.
"""

import math


def movie(card, ticket, perc):
    """
    Calculates the minimum number of cinema visits for System B to be cheaper than System A.

    Parameters:
    - card (int/float): The initial cost of the card for System B.
    - ticket (int/float): The regular price of a single ticket.
    - perc (int/float): The percentage discount for subsequent tickets in System B.

    Returns:
    - int: The first number of visits where System B (rounded up) is cheaper.
    """
    n = 0
    cost_A = 0
    cost_B = card

    while math.ceil(cost_B) >= cost_A:
        n += 1
        cost_A = n * ticket
        cost_B += ticket * (perc ** n)

    return n
