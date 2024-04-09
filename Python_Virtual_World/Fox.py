from MyVector import MyVector
from Animal import Animal


class Fox(Animal):


    STRENGTH = 3
    INITIATIVE = 7


    def __init__(self, position: MyVector):
        super().__init__(position, Fox.STRENGTH, Fox.INITIATIVE)


    def isSmelling(self):

        return True


    def draw(self) -> str:

        return "orange"


    def __str__(self):
        return "Fox"