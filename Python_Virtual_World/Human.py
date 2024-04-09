from random import random

from MyVector import MyVector
from Animal import Animal
from World import World


class Human(Animal):


    STRENGTH = 5
    INITIATIVE = 4
    SPECIALROUNDS = 5
    ROUNDSDOWN = 2

    def __init__(self, position: MyVector):
        super().__init__(position, Human.STRENGTH, Human.INITIATIVE)
        self.__specialRounds = 0


    def action(self):
        if self.__specialRounds > Human.ROUNDSDOWN :

            for y in range(-1,2):

                for x in range(-1, 2):

                    org = self._world.getOrganismAt(self.getPosition() + MyVector(y,x))

                    if org != None and org.isAlive() and not isinstance(org, Human):
                        org.kill()
                        self._world.getNots().add("Human has burned " + org.__str__())


        self.__specialRounds -= 1
        self.__specialRounds = 0 if self.__specialRounds <= 0 else self.__specialRounds

        move = self._world.popMove()

        if move == World.Move.Up:

            self._changeLocation(MyVector(-1, 0))

        elif move == World.Move.Down:

            self._changeLocation(MyVector(1, 0))

        elif move == World.Move.Left:

            self._changeLocation(MyVector(0, -1))

        elif move == World.Move.Right:

            self._changeLocation(MyVector(0, 1))

        elif move == World.Move.Ult:

            self.__specialRounds = Human.SPECIALROUNDS if self.__specialRounds == 0 else self.__specialRounds


    def draw(self) -> str:

        return "#FFFD96"


    def __str__(self):
        return "Human"

    def getSpecialRounds(self):
        return self.__specialRounds

    def setSpecialRounds(self, rounds : int):
        self.__specialRounds = rounds