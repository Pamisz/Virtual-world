from MyVector import MyVector
from Plant import Plant


class Dandelion(Plant):


    STRENGTH = 0
    TRIES = 3

    def __init__(self, position : MyVector):
        super().__init__(position, Dandelion.STRENGTH)


    def action(self):

        for i in range(Dandelion.TRIES):

            self.spread()

    def draw(self) -> str:

        return "yellow"


    def __str__(self):

        return "Dandelion"

