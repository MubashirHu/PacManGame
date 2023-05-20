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
        

    def _initialize(self):
        #self._root.configure(bg = 'black')
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
            add_shape(self, x_coordinate, y_coordinate, self._shape_size, "circle", 'yellow')
        else:
            print("ERROR")