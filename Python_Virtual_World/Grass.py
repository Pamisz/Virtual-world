from MyVector import MyVector
from Plant import Plant


class Grass(Plant):


    STRENGTH = 0

    def __init__(self, position : MyVector):
        super().__init__(position, Grass.STRENGTH)


    def draw(self) -> str:

        return "green"


    def __str__(self):

        return "Grass"

