#This file contains the build of the GUI
from tkinter import *
from src.util import *
import time 
class View:

    def __init__(self):
        #GUI window
        self._root = Tk()
        self._canvas = None 
        self._shape_size = 25
        self._pellet_size = 25
        self._wall_color = "blue"
        self._pellet_color = "purple"
        self._pacman_color = "yellow"
        self._ghost_house_path_color = "green"
        self._ghost_house_base_color = "white"

    def _initialize(self):
        self._root.title('PacMan Game')
        self._root.geometry('1300x1300')

        self._canvas = Canvas(self._root, width=1200, height=1200, bg='black')
        self._canvas.pack()
        return 1
    
    def _draw_shape(self, y_coordinate, x_coordinate, shape):
        if (shape == gamePiece._pellet):
            if self.add_shape(self, x_coordinate, y_coordinate, self._pellet_size, gamePiece._pellet, self._pellet_color):
                return 1
            else:
                return 0
            
        elif(shape == gamePiece._wall):
            if self.add_shape(self, x_coordinate, y_coordinate, self._shape_size, gamePiece._wall, self._wall_color):
                return 1
            else:
                return 0
            
        elif(shape == gamePiece._pacman):
            if self._draw_pacman_in_position(x_coordinate, y_coordinate):
                if self._eat_pellet_in_position(x_coordinate, y_coordinate):
                    return 1
                else:
                    return 0
            else:
                return 0
            
        elif(shape == gamePiece._ghost_house_path):
            if self.add_shape(self, x_coordinate, y_coordinate, self._shape_size, gamePiece._ghost_house, self._ghost_house_path_color):
                return 1
            else:
                return 0
            
        elif(shape == gamePiece._ghost_blinky_home):
            if self.add_shape(self, x_coordinate, y_coordinate, self._shape_size, gamePiece._ghost_house, self._ghost_house_base_color):
                return 1
            else:
                return 0
            
        elif(shape == gamePiece._ghost_inky_home):
            if self.add_shape(self, x_coordinate, y_coordinate, self._shape_size, gamePiece._ghost_house, self._ghost_house_base_color):
                return 1
            else:
                return 0
            
        elif(shape == gamePiece._ghost_pinky_home):
            if self.add_shape(self, x_coordinate, y_coordinate, self._shape_size, gamePiece._ghost_house, self._ghost_house_base_color):
                return 1
            else:
                return 0
            
        elif(shape == gamePiece._ghost_clyde_home):
            if self.add_shape(self, x_coordinate, y_coordinate, self._shape_size, gamePiece._ghost_house, self._ghost_house_base_color):
                return 1
            else:
                return 0
            
        elif (shape == gamePiece._ghost):
            if self.add_shape(self, x_coordinate, y_coordinate, self._shape_size, gamePiece._ghost, self._ghost_house_base_color):
                return 1
            else:
                return 0
        else:
            print("ERROR: Unidentified shape")
            return 0
        
    def _draw_ghost(self, y_coordinate, x_coordinate, ghost_obj):
            if self.add_shape(self, x_coordinate, y_coordinate, self._shape_size, gamePiece._ghost, ghost_obj._color):
                return 1
            else:
                return 0

    def _draw_pacman_in_position(self, x_coordinate, y_coordinate):
        self._canvas.delete(gamePiece._pacman)
        if self.add_shape(self, x_coordinate, y_coordinate, self._shape_size, gamePiece._pacman, self._pacman_color):
            return 1
        else:
            return 0
    
    def _eat_pellet_in_position(self, x_coordinate, y_coordinate):
        pellet_id = self._canvas.find_withtag(f"{x_coordinate}_{y_coordinate}")
        if pellet_id:
            self._canvas.delete(pellet_id)
            return 1
        else:
            return 0
        
    def add_shape(self, tk_obj, i,j, size, gamepiece, color):
        if gamepiece == gamePiece._pacman:
            x0 = i * size
            y0 = j * size 
            x1 = x0 + size 
            y1 = y0 + size 
            self._canvas.create_oval(x0, y0, x1, y1, tags= gamePiece._pacman, fill=color)
            return 1

        if gamepiece == gamePiece._pellet:
            x0 = i * size
            y0 = j * size
            x1 = x0 + size 
            y1 = y0 + size
            self._canvas.create_oval(x0, y0, x1, y1, tags= f"{i}_{j}", fill=color)
            return 1

        elif gamepiece == gamePiece._wall:
            x0 = i * size
            y0 = j * size
            x1 = x0 + size
            y1 = y0 + size
            self._canvas.create_rectangle(x0, y0, x1, y1, fill=color)
            return 1

        elif gamepiece == gamePiece._ghost_house:
            x0 = i * size
            y0 = j * size
            x1 = x0 + size
            y1 = y0 + size
            self._canvas.create_rectangle(x0, y0, x1, y1, fill=color)
            return 1
        elif gamepiece == gamePiece._ghost:
            x0 = i * size
            y0 = j * size
            x1 = x0 + size
            y1 = y0 + size
            self._canvas.create_rectangle(x0, y0, x1, y1, fill=color)
            return 1
        else:
            return 0