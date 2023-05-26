#This file contains the build of the GUI
from tkinter import *
from src.util import *
import time 
class View:

    def __init__(self):
        #GUI window
        self._root = Tk()
        self._canvas = None 
        self._shape_size = 30
        self._pellet_size = 30
        self._wall_color = "blue"
        self._path_color = "black"
        self._pellet_color = "white"
        self._pacman_color = "yellow"
        self._path_covered_color = "purple"
        self._ghost_house_color = "white"

    def _initialize(self):
        self._root.title('PacMan Game')
        self._root.geometry('1300x1300')

        self._canvas = Canvas(self._root, width=1200, height=1200, bg='black')
        self._canvas.pack()
        return 1
    
    def _draw_shape(self, y_coordinate, x_coordinate, shape):
        if (shape == gamePiece._pellet):
            self.add_shape(self, x_coordinate, y_coordinate, self._pellet_size, "pellet", self._pellet_color)
            print('good pellet')
            return 1
        elif(shape == gamePiece._wall):
            self.add_shape(self, x_coordinate, y_coordinate, self._shape_size, "wall", self._wall_color)
            print('good wall')
            return 1
        elif(shape == gamePiece._pacman):
            self._draw_pacman_in_position(x_coordinate, y_coordinate)
            print('good pman')
            return 1
        elif(shape == gamePiece._ghost_house):
            self.add_shape(self, x_coordinate, y_coordinate, self._shape_size, "ghost house", self._ghost_house_color)
            print('good house')
            return 1
        else:
            print("ERROR: Unidentified shape")
            return 0
  
    def _draw_pacman_in_position(self, x_coordinate, y_coordinate):
        self._canvas.delete("pacman")
        self.add_shape(self, x_coordinate, y_coordinate, self._shape_size, "pacman", self._pacman_color)

        shape_ids = self._canvas.find_withtag(f"{x_coordinate}_{y_coordinate}")
        if shape_ids:
            self._canvas.delete(shape_ids[0])
        else:
            return None  # No shape found with the given coordinates

    def add_shape(self, tk_obj, i,j, size, shape, color):
        if shape == "pacman":
            x0 = i * size
            y0 = j * size 
            x1 = x0 + size 
            y1 = y0 + size 
            self._canvas.create_oval(x0, y0, x1, y1, tags="pacman", fill=color)

        if shape == "pellet":
            x0 = i * size
            y0 = j * size
            x1 = x0 + size
            y1 = y0 + size
            self._canvas.create_oval(x0, y0, x1, y1, tags= ("pellet", i,j), fill=color)
        elif shape == "wall":
            x0 = i * size
            y0 = j * size
            x1 = x0 + size
            y1 = y0 + size
            self._canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        elif shape == "ghost house":
            x0 = i * size
            y0 = j * size
            x1 = x0 + size
            y1 = y0 + size
            self._canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        else:
            pass