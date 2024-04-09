import copy
from random import random

from MyVector import MyVector
from Organism import Organism


class Plant(Organism):

    INITIATIVE = 0
    PROPABILITY = 0.05

    def __init__(self, position: MyVector, s: int):
        super().__init__(position, s, Plant.INITIATIVE)

    def action(self):

        self.spread()

    def collision(self):

        pass

    def newRound(self):

        pass


    def spread(self):

        if random() >= Plant.PROPABILITY:
            return

        newField = self._world.getFreeRandomSquare(self.getPosition())

        if newField is None:
            return

        org = copy.deepcopy(self)

        org.setAge(0)
        org.setPosition(newField)

        self._world.addOrg(org)
        self._world.getNots().add(self.__str__() + " has spreaded!")




