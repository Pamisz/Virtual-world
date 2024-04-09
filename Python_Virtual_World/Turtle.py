from random import random

from MyVector import MyVector
from Animal import Animal
from Organism import Organism


class Turtle(Animal):


    STRENGTH = 2
    INITIATIVE = 1
    PROPABILITY = 0.25
    DEFENSE = 5


    def __init__(self, position : MyVector):
        super().__init__(position, Turtle.STRENGTH, Turtle.INITIATIVE)


    def action(self):

        if random() < Turtle.PROPABILITY:
            self._RandomMove()


    def didBlocked(self,other : Organism) -> bool:

        if other.getStrength() < Turtle.DEFENSE:
            self._world.getNots().add("Turtle has blocked the " + other.__str__())
            return True
        return False



    def draw(self) -> str:

        return "#438C7E"


    def __str__(self):
        return "Turtle"
