import copy
from random import randint

from Notifications import Notifications
from MyVector import MyVector
from Organism import Organism

from enum import Enum

class World:

    class Move(Enum):
        Up = 0
        Down = 1
        Left = 2
        Right = 3
        Ult = 4
        Stand = 5

    def __init__(self, height: int, width: int, organisms=None):

        if organisms is None:
            organisms = []
        else:
            for org in organisms:
                org.setWorld(self)

        self.__height = height
        self.__width = width
        self.__organisms = organisms
        self.__round = 0
        self.__nots = Notifications()
        self.__move = World.Move.Stand


    def getHeight(self):
        return self.__height

    def getWidth(self):
        return self.__width

    def getOrganisms(self):
        return self.__organisms

    def getRound(self):
        return self.__round

    def getNots(self):
        return self.__nots

    def getMove(self):
        return self.__move


    def setRound(self, value):
        self.__round = value

    def setMove(self, move : Move):
        self.__move = move

    def popMove(self):

        tmp = copy.deepcopy(self.__move)
        self.__move = World.Move.Stand

        return tmp


    def addOrg(self, org: Organism):
        org.setWorld(self)
        self.__organisms.append(org)
  

    def getCollision(self, org):

        tmp =  [x for x in self.__organisms if x.getPosition() == org.getPosition() and x != org]

        if len(tmp):
            return tmp[0]

        return None


    def __actions(self):

        self.__organisms = sorted(self.__organisms,reverse=True, key= lambda x: x.getAge())
        self.__organisms = sorted(self.__organisms, reverse=True, key= lambda x: x.getInitiative())

        for org in self.__organisms:

            if org.isAlive():

                org.action()
                org.collision()

            org.ageUp()


    def runRound(self):

        self.__nots.clear()

        for org in self.__organisms:
            org.newRound()

        self.__round+=1
        self.__actions()

        self.__organisms = [x for x in self.__organisms if x.isAlive()]


    def getOrganismAt(self, position : MyVector) -> Organism:

        wanted = None

        for org in self.__organisms:

            if org.getPosition() == position and org.isAlive():

                if wanted is None or wanted.getStrength() < org.getStrength():

                    wanted = org

        return wanted


    def getFreeSquare(self, position : MyVector, range = 1):

        for dy in [-1 * range, 0, range]:

            for dx in [-1 * range, 0, range]:

                point =  MyVector(dy,dx) + position

                if point != position \
                        and self.getOrganismAt(point) is None \
                        and not point.outside(self.getHeight(),self.getWidth()):
                    return point

        return position


    def getFreeRandomSquare(self, position : MyVector, range = 1):

        points = []

        for dy in [-1 * range, 0, range]:

            for dx in [-1 * range, 0, range]:

                point =  MyVector(dy, dx) + position

                if point != position \
                        and self.getOrganismAt(point) is None \
                        and not point.outside(self.getHeight(),self.getWidth()):
                    points.append(point)

        if len(points):
            return points[randint(0,len(points) - 1)]

        return None



    




