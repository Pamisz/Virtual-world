from MyVector import MyVector
from Organism import Organism
from Plant import Plant


class NightShade(Plant):


    STRENGTH = 0

    def __init__(self, position : MyVector):
        super().__init__(position, NightShade.STRENGTH)

    def giveMod(self, other : Organism):

        other.kill()



    def draw(self) -> str:

        return "#31004C"


    def __str__(self):

        return "NightShade"

