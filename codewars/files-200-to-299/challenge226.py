"""
Given an array of positive integers (the weights of the people),
return a new array / tuple of two integers (depending on your language),
whereby the first one is the total weight of team 1, and the second one
is the total weight of team 2. Note that the array will never be empty.
"""


def row_weights(array):
    team1 = sum(array[i] for i in range(0, len(array), 2))  # Sum of weights for team 1 (even indices).
    team2 = sum(array[i] for i in range(1, len(array), 2))  # Sum of weights for team 2 (odd indices).
    return (team1, team2)
