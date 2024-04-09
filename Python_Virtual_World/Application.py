import tkinter as tk
from World import World
from Organism import Organism
from MyVector import MyVector
from tkinter.messagebox import showinfo
from tkinter import ttk, messagebox, filedialog
from File import File

from Antelope import Antelope
from CyberSheep import CyberSheep
from Sheep import Sheep
from Human import Human
from Wolf import Wolf
from Human import Human
from Turtle import Turtle
from Fox import Fox

from Dandelion import Dandelion
from NightShade import NightShade
from PineBorsht import PineBorsht
from Grass import Grass
from Guarana import Guarana

class Application(tk.Frame) :
    def __init__(self, master = None, size = 20, cell_size = 30) :
        super().__init__(master)
        self.size = size
        self.cell_size = cell_size
        self.canvas = tk.Canvas(self, width = size * cell_size, height = size * cell_size + 10)
        self.canvas.pack()
        self.world = World(20,20)
        self.basic()
        self.draw_board()
        self.file = File()
        self.events()
        self.focus_set()

        button_frame = tk.Frame(self)
        button_frame.pack(side = tk.BOTTOM)

        self.new_game_button = tk.Button(self, text = "Next round", command = self.gogo)
        self.new_game_button.pack(side = tk.LEFT)

        self.notifications_button = tk.Button(self, text = "Notifications", command = self.nots)
        self.notifications_button.pack(side = tk.LEFT)

        self.menu_button = tk.Menubutton(self, text = "Options")
        self.menu = tk.Menu(self.menu_button, tearoff = False)
        self.menu.add_command(label = "Load", command = self.load)
        self.menu.add_command(label = "Save", command = self.save)
        self.menu_button.configure(menu = self.menu)
        self.menu_button.pack(side = tk.RIGHT)

    def draw_board(self) :
        for row in range(self.size) :
            for col in range(self.size) :
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                color = "cyan"

                for org in self.world.getOrganisms():
                    if (org.getPosition().getX() == col and org.getPosition().getY() == row) :
                        color = org.draw()


                self.canvas.create_rectangle(x1, y1, x2, y2, fill = color)


    def AddOrganism(self, name : str, x : int, y : int) :
        if name == "Wolf":
                    self.world.addOrg( Wolf(MyVector(y , x)))
        elif name == "Turtle":
                    self.world.addOrg( Turtle(MyVector(y , x)))
        elif name == "Antelope":
                    self.world.addOrg( Antelope(MyVector(y , x)))
        elif name == "Sheep":
                    self.world.addOrg( Sheep(MyVector(y , x)))
        elif name == "Fox":
                    self.world.addOrg( Fox(MyVector(y , x)))
        elif name == "CyberSheep":
                    self.world.addOrg( CyberSheep(MyVector(y , x)))
        elif name == "Dandelion":
                    self.world.addOrg( Dandelion(MyVector(y , x)))
        elif name == "Grass":
                    self.world.addOrg( Grass(MyVector(y , x)))
        elif name == "Guarana":
                    self.world.addOrg( Guarana(MyVector(y , x)))
        elif name == "NightShade":
                    self.world.addOrg( NightShade(MyVector(y , x)))
        elif name == "PineBorsht":
                    self.world.addOrg( PineBorsht(MyVector(y , x)))

    def events(self) :

        def move(event) :
            if event.keysym == "Up":
                self.world.setMove(World.Move.Up)
                self.world.getNots().add("Next move is up.")
           
            elif event.keysym == "Down":
                    self.world.setMove(World.Move.Down)
                    self.world.getNots().add("Next move is down.")

            elif event.keysym == "Left":
                    self.world.setMove(World.Move.Left)
                    self.world.getNots().add("Next move is left.")

            elif event.keysym == "Right":
                    self.world.setMove(World.Move.Right)
                    self.world.getNots().add("Next move is right.")

            elif event.keysym == "r":
                    self.world.setMove(World.Move.Ult)
                    self.world.getNots().add("Ult has been activated!")

        self.canvas.bind("<Button-1>", self.on_cell_click)
        self.bind("<Key>",move)

    def on_cell_click(self, event) :
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        for org in self.world.getOrganisms() :
            if isinstance(org, Organism) and org.getPosition().getX() == col and org.getPosition().getY() == row and org.isAlive() :
                showinfo("Error", "U can't add an organism here, this place is taken, by: " + org.__str__() + "!")
                return
        self.show_menu(col, row)

    def gogo(self):
        self.world.runRound()
        self.draw_board()

    def nots(self):
        nots = self.world.getNots().load()
        showinfo("Notifications", nots)

    def show_menu(self, x, y) :
        menu = tk.Menu(self, tearoff = False)
        menu.add_command(label = "Antelope", command = lambda: self.AddOrganism("Antelope", x, y))
        menu.add_command(label = "CyberSheep", command = lambda: self.AddOrganism("CyberSheep", x, y))
        menu.add_command(label = "Sheep", command = lambda: self.AddOrganism("Sheep", x, y))
        menu.add_command(label = "Fox", command = lambda: self.AddOrganism("Fox", x, y))
        menu.add_command(label = "Wolf", command = lambda: self.AddOrganism("Wolf", x, y))
        menu.add_command(label = "Turtle", command = lambda: self.AddOrganism("Turtle", x, y))
        menu.add_command(label = "====================", command = None)
        menu.add_command(label = "PineBorsht", command = lambda: self.AddOrganism("PineBorsht", x, y))
        menu.add_command(label = "Guarana", command = lambda: self.AddOrganism("Guarana", x, y))
        menu.add_command(label = "Dandelion", command = lambda: self.AddOrganism("Dandelion", x, y))
        menu.add_command(label = "Grass", command = lambda: self.AddOrganism("Grass", x, y))
        menu.add_command(label = "NightShade", command = lambda: self.AddOrganism("NightShade", x, y))
        menu.post(x, y)

    def save(self) :
        fname = filedialog.asksaveasfilename()
        if fname == "":
            return
        self.file.save(self.world, fname)
        showinfo("Successful save", "Game has been saved!")

    def load(self) : 
        fname = filedialog.askopenfilename()
        if fname == "":
            return
        w = self.file.load(fname)
        if w is None:
            messagebox.showerror("Error","File error")
            return

        self.world = w
        self.draw_board()
        showinfo("Successful load", "Game has been loaded!")

    def basic(self) :
        self.world.addOrg(Wolf(MyVector(1, 1)))
        self.world.addOrg(Wolf(MyVector(3, 1)))

        self.world.addOrg(Turtle(MyVector(5, 5)))
        self.world.addOrg(Turtle(MyVector(7, 5)))

        self.world.addOrg(Sheep(MyVector(10, 7)))
        self.world.addOrg(Sheep(MyVector(13, 7)))

        self.world.addOrg(Fox(MyVector(15, 10)))
        self.world.addOrg(Fox(MyVector(17, 10)))

        self.world.addOrg(Antelope(MyVector(18, 12)))
        self.world.addOrg(Antelope(MyVector(19, 12)))

        self.world.addOrg(CyberSheep(MyVector(2, 8)))
        self.world.addOrg(CyberSheep(MyVector(12, 6)))

        self.world.addOrg(Dandelion(MyVector(19, 0)))
        self.world.addOrg(Dandelion(MyVector(19, 19)))

        self.world.addOrg(Grass(MyVector(1, 10)))
        self.world.addOrg(Grass(MyVector(19, 10)))

        self.world.addOrg(Guarana(MyVector(10, 15)))
        self.world.addOrg(Guarana(MyVector(10, 18)))

        self.world.addOrg(NightShade(MyVector(16, 8)))
        self.world.addOrg(NightShade(MyVector(9, 15)))

        self.world.addOrg(PineBorsht(MyVector(19, 0)))
        self.world.addOrg(PineBorsht(MyVector(15, 18)))

        self.world.addOrg(Human(MyVector(10, 19)))

root = tk.Tk()
root.title("Patryk Miszke 193249")

app = Application(root)
app.pack()




