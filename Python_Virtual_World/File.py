import copy

from MyVector import MyVector
from Organism import Organism
from World import World

from Antelope import Antelope
from CyberSheep import CyberSheep
from Sheep import Sheep
from Human import Human
from Wolf import Wolf
from Turtle import Turtle
from Fox import Fox

from Dandelion import Dandelion
from NightShade import NightShade
from PineBorsht import PineBorsht
from Grass import Grass
from Guarana import Guarana



class File:

    def save(self, world: World, name: str):

        with open(name, "w") as out:

            out.write(f"{world.getRound()} {world.getHeight()} {world.getWidth()} \n")

            for org in world.getOrganisms():

                out.write(f"{str(org)} {org.getAge()} {org.getPosition().getY()} {org.getPosition().getX()}")

                if isinstance(org, Human):
                    out.write(f" {org.getSpecialRounds()}")

                out.write("\n")

    def load(self, name):

        try:
            with open(name, "r") as input:
                r = input.read().split("\n")
             
                r = [char for char in r if char != ""]
                
                buffer = [char for char in r[0].split(" ")]
                
                wrd = World(int(buffer[1]), int(buffer[2]), None)
                wrd.setRound(int(buffer[0]))

                for i in range(1, len(r)):
                    org = self.__loadOrg(r[i])
                    wrd.addOrg(org)

                return wrd


        except:
      
            return None

    def __loadOrg(self, line: str) -> Organism:

        args = line.split(" ")

        org = self.__alocByName(args[0])

        if org is None:
            raise Exception

        org.setAge(int(args[1]))
        org.setPosition(MyVector(int(args[2]),int(args[3])))

        if isinstance(org, Human):
            org.setSpecialRounds(int(args[4]))

        return org

    def __alocByName(self, name: str):

        p0 = MyVector(0, 0)

        organisms = [
            Human(p0),
            Wolf(p0),
            Sheep(p0),
            CyberSheep(p0),
            Fox(p0),
            Turtle(p0),
            Antelope(p0),
            Grass(p0),
            Dandelion(p0),
            Guarana(p0),
            NightShade(p0),
            PineBorsht(p0)
        ]

        for org in organisms:
            if str(org) == name:
                return copy.deepcopy(org)

        return None