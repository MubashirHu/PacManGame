#This file contains the build of the GUI
from tkinter import *
from src.util import *
class View:

    def __init__(self):

        #GUI window
        self._root = Tk()
        self._canvas = None 
        self._shape_size = 50
        self._wall_color = "blue"
        self._path_color = "black"
        self._pacman_color = "yellow"
        
    def _initialize(self):
        self._root.title('PacMan Game')
        self._root.geometry('800x1000')

        self._canvas = Canvas(self._root, width=800, height=1000, bg='white')
        self._canvas.pack()

    def _draw_shape(self, x_coordinate, y_coordinate, shape):

        if (shape == 1):
            add_shape(self, x_coordinate, y_coordinate, self._shape_size, "square", self._wall_color)
        elif(shape == 0):
            add_shape(self, x_coordinate, y_coordinate, self._shape_size, "square", self._path_color)
        elif(shape == 2):
            self._canvas.delete("pacman")
            add_shape(self, x_coordinate, y_coordinate, self._shape_size, "circle", self._pacman_color)
        else:
            print("ERROR: Unidentified shape")

    def _update_pacman_position(self, x_coordinate, y_coordinate):
        self._canvas.delete("pacman")
        add_shape(self, x_coordinate, y_coordinate, self._shape_size, "circle", self._pacman_color)

        