""
Color Ghost

Create a class Ghost

Ghost objects are instantiated without any arguments.

Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated.

ghost = Ghost()
ghost.color  #=> "white" or "yellow" or "purple" or "red"
"""

import random


class Ghost:
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        self.color = random.choice(colors)

# Example usage:
ghost1 = Ghost()
print(ghost1.color)

ghost2 = Ghost()
print(ghost2.color)
