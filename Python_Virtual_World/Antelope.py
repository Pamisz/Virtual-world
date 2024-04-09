from random import random

from MyVector import MyVector
from Animal import Animal


class Antelope(Animal):


    STRENGTH = 4
    INITIATIVE = 4
    RANGE = 2
    PROPABILITY = 0.5


    def __init__(self, position : MyVector):
        super().__init__(position, Antelope.STRENGTH, Antelope.INITIATIVE)


    def action(self):

        self._RandomMove(Antelope.RANGE)

    def didEscape(self) -> bool:

        if random() < Antelope.PROPABILITY:
            self._world.getNots().add(self.__str__() + " has escaped!")


    def draw(self) -> str:

        return "#964B00"


    def __str__(self):

        return "Antelope"