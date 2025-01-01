"""
Classy Extensions

Classy Extensions, this kata is mainly aimed at the new JS ES6 Update introducing extends keyword.
You will be preloaded with the Animal class, so you should only edit the Cat class.

Task

Your task is to complete the Cat class which Extends Animal and replace the speak method to
return the cats name + meows. e.g. 'Mr Whiskers meows.'
"""

from preloaded import Animal


class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."
