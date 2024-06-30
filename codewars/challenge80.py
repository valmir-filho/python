"""
In this kata, your task is to implement an
extended version of the famous rock-paper-scissors game.
"""


def rpsls(pl1, pl2):
    # Dictionary to store the winning cases.
    rules = {
        "scissors": ["paper", "lizard"],
        "paper": ["rock", "spock"],
        "rock": ["lizard", "scissors"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }

    if pl1 == pl2:
        return "Draw!"
    elif pl2 in rules[pl1]:
        return "Player 1 Won!"
    else:
        return "Player 2 Won!"
