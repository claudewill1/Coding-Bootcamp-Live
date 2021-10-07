
import random
import math

class Pirate:

    def __init__(self,name) -> None:
        self.name = name
        self.strength = 10
        self.speed = 4
        self.health = 100

    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}")

    def attack(self,ninja):
        ninja.health -= self.strength
        ninja.defend(self)
        return self

    def defend(self,ninja):
        rng = random.randint(1,2)
        if rng == 2:
            ninja.health -= math.round(self.strength/2)
            print(f"{self.name} defended against {ninja.name}nHealth: {self.health}\n{ninja.name}\nHealth: {ninja.health}")
        else:
            print(f"{self.name} Faield to defend against {ninja.name}\n{ninja.health} Health: {ninja.health}")