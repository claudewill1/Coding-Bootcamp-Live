import random
import math

class Ninja:

    def __init__(self,name) -> None:
        self.name = name
        self.strength = 15
        self.speed = 5
        self.health = 100

    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}")

    def attack(self, pirate):
        pirate.health -= self.strength
        pirate.defend(self)
        return self

    def defend(self,pirate):
        rng = random.randint(1,2)
        if rng == 2:
            pirate.health -= math.round(self.strength/2)
            print(f"{self.name} defended against {math.pi.name}nHealth: {self.health}\n{pirate.name}\nHealth: {pirate.health}")
        else:
            print(f"{self.name} Faield to defend against {pirate.name}\n{pirate.health} Health: {pirate.health}")