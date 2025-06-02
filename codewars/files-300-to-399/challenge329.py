"""
Ahoy matey!

You are a leader of a small pirate crew. And you have a plan. With the help of OOP you wish to make a pretty efficient system to identify ships with heavy booty on board!

Unfortunately for you, people weigh a lot these days, so how do you know if a ship is full of gold and not people?

You begin with writing a generic Ship class / struct:

class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
        
Every time your spies see a new ship enter the dock, they will create a new ship object based on their observations:

- draft - an estimate of the ship's weight based on how low it is in the water;
- crew - the count of crew on board;
- Titanic = Ship(15, 10).

Task:

You have access to the ship "draft" and "crew". "Draft" is the total ship weight and "crew" is the number of humans on the ship.

Each crew member adds 1.5 units to the ship draft. If after removing the weight of the crew, the draft is still more than 20, then the ship is worth looting. Any ship weighing that much must have a lot of booty!

Add the method is_worth_it to decide if the ship is worthy to loot. 
"""


class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

  
    def is_worth_it(self):
        # Cada tripulante adiciona 1.5 unidades ao draft.
        real_draft = self.draft - (self.crew * 1.5)
        return real_draft > 20
