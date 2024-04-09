from ast import BitAnd
import copy
from random import randint
from MyVector import MyVector
from Organism import Organism


class Animal(Organism):


    def __init__(self, position : MyVector, s : int, i : int):

        super().__init__(position, s, i)
        self._didMultiply = False
        self._prev = position


    def action(self):

        self._RandomMove()


    def collision(self):

        opponent = self._world.getCollision(self)

        if opponent is None:
            return

        if str(opponent) == str(self):

            self._multiply(opponent)
            return

        self._fight(opponent)


    def newRound(self):

        self._didMultiply = False



    def _RandomMove(self, range = 1):


        if self.isSmelling() and self.everyoneStronger():
            return

        cords = [-1 * range, 0,range]
        prev = MyVector(self._position.getY(), self._position.getX())

        while True:

            randX = cords[randint(0,2)]
            randY = cords[randint(0,2)]

            d = MyVector(randY,randX)

            self._changeLocation(d)

            if not (prev == self._position or
                    (self.isSmelling() and
                     self._world.getCollision(self) is not None and
                     self._world.getCollision(self).getStrength() > self.getStrength())):
                break

    def _changeLocation(self, d : MyVector):

        if not (self.getPosition() + d) \
            .outside(self._world.getHeight(), self._world.getWidth()):

            self._prev = MyVector(self._position.getY(), self._position.getX())
            self._position += d


    def _multiply(self, crush):

        if crush.getAge() == 0:
            return

        org = copy.deepcopy(self)
        self.__reverse()

        birthField = self._world.getFreeSquare(crush.getPosition())

        if birthField == crush.getPosition() or crush._didMultiply or self._didMultiply:
            return


        org.setPosition(birthField)
        org.setAge(-1)

        self._world.addOrg(org)
        self._world.getNots().add(org.__str__() + " was born!")

        self._didMultiply = True
        crush._didMultiply = True


    def __reverse(self):
        self.setPosition(self._prev)

    def _fight(self, opponent : Organism):

        if self.escape() or opponent.escape():
            return

        if self.getStrength() < opponent.getStrength():

            if self.didBlocked(opponent):

                self.__reverse()
                return

            self._world.getNots().add(f"{str(opponent)} has eaten {str(self)}")
            self.kill()
            self.giveMod(opponent)

            return

        if opponent.didBlocked(self):

            self.__reverse()
            return

        self._world.getNots().add(f"{str(self)} has eaten {str(opponent)}")
        opponent.kill()
        opponent.giveMod(self)

    def everyoneStronger(self) -> bool:

        for y in range(-1,2):
            for x in range(-1,2):

                field = MyVector(y,x)

                org = self._world.getOrganismAt(self.getPosition() + field)

                if org != self and (org is None or org.getStrength() <= self.getStrength()):

                    return False


        return True




