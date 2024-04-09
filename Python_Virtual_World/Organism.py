from abc import ABC, abstractmethod

from MyVector import MyVector


class Organism(ABC):


    def __init__(self, position : MyVector, s : int, i : int):

        self._position = position
        self._strength = s
        self._initiative = i
        self._alive = True
        self._age = 0



    def getPosition(self):

        return self._position


    def setPosition(self, p : MyVector):

        self._position = p


    def getInitiative(self):

        return self._initiative


    def getStrength(self):

        return self._strength


    def setStrength(self, s : int):

        self._strength = s


    def getAge(self):

        return self._age

    def setAge(self, a: int):

        self._age = a
    

    def setWorld(self, w):

        self._world = w


    def isAlive(self) -> bool:

        return self._alive


    def kill(self):

        self._world.getNots().add(f"{str(self)} is dead")
        self._alive = False


    def giveMod(self, other):

        pass


    def didBlocked(self,other) -> bool:

        return False

    def isResistance(self) -> bool:

        return False


    def didEscape(self) -> bool:

        return False

    def escape(self) -> bool:

        if self.didEscape():

            newField = self._world.getFreeSquare(self._position)

            if newField == self._position:

                return False

            self.setPosition(newField)

            return True

        return False



    def isSmelling(self):

        return False


    def ageUp(self):

        self._age+=1


    @abstractmethod
    def __str__(self):
        pass


    @abstractmethod
    def action(self):

        pass


    @abstractmethod
    def collision(self):

        pass


    @abstractmethod
    def draw(self) -> str:

        pass


    @abstractmethod
    def newRound(self):

        pass




