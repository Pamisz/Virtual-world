from MyVector import MyVector
from Animal import Animal
from PineBorsht import PineBorsht


class CyberSheep(Animal):


    STRENGTH = 11
    INITIATIVE = 4

    def __init__(self, position: MyVector):
        super().__init__(position, CyberSheep.STRENGTH, CyberSheep.INITIATIVE)

    def action(self):

        minPos = self.getPosition()

        for org in self._world.getOrganisms():
            if isinstance(org,PineBorsht):

                pos = org.getPosition()
                if minPos == self.getPosition() or \
                        (minPos - self.getPosition()).len() > (pos - self.getPosition()).len():

                    minPos = pos

        if minPos == self.getPosition():
            super().action()
            return

        tmp = minPos-self.getPosition()
        tmp = tmp.normalised()

        self._changeLocation(tmp)


    def isResistance(self) -> bool:

        return True

    def newRound(self):

        pass


    def draw(self) -> str:

        return "#555652"

    def __str__(self):

        return "CyberSheep"