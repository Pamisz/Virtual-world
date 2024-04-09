from MyVector import MyVector
from Organism import Organism
from Plant import Plant
from Animal import Animal


class PineBorsht(Plant):


    STRENGTH = 0

    def __init__(self, position : MyVector):
        super().__init__(position, PineBorsht.STRENGTH)


    def action(self):

        for y in range(-1,2):

            for x in range(-1, 2):

                org = self._world.getOrganismAt(self.getPosition() + MyVector(y,x))

                if isinstance(org,Animal) and not org.isResistance():
                    org.kill()


        super().action()


    def giveMod(self, other : Organism):

        if other.isResistance():
            return

        other.kill()


    def draw(self) -> str:

        return "white"


    def __str__(self):

        return "PineBorsht"