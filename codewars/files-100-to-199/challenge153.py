"""
Create a combat function that takes the player's current
health and the amount of damage received, and returns the
player's new health. Health can't be less than 0.
"""


def combat(health, damage):
    # Calculate the new health after damage.
    new_health = health - damage
    # Ensure health doesn't drop below 0.
    if new_health < 0:
        new_health = 0
    return new_health
