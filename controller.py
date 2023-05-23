#This file is the brain of the file and relays information to and from the model.py and view.py
from model import *
from view import *
from src.util import *
import os
import time
class Controller:
    def __init__(self):
        self.my_model = Model()
        self.my_view = View()

    def _initialize_game(self):
        if self.my_model._initialize():
            self.my_view._initialize()
            print("Both view and model have been initialized...")

    def _display_game(self):
        for i in range(self.my_model.Map._rows):
            for j in range(self.my_model.Map._columns):
                location_and_shape = self.my_model._check_for_walls_and_path(i, j)       
                self.my_view._draw_shape(location_and_shape[0], location_and_shape[1], location_and_shape[2])
        
        self.my_view._draw_shape(self.my_model.Pacman._position[0], self.my_model.Pacman._position[1], 2)
    
    def _update_pacman_position(self, direction):
        if(direction == "w"):
            self.my_view._draw_shape(self.my_model.Pacman._position[0], self.my_model.Pacman._position[1]-1, 2)
        if(direction == "a"):
            self.my_view._draw_shape(self.my_model.Pacman._position[0]-1, self.my_model.Pacman._position[1], 2)
        if(direction == "s"):
            self.my_view._draw_shape(self.my_model.Pacman._position[0], self.my_model.Pacman._position[1]+1, 2)
        if(direction == "d"):
            self.my_view._draw_shape(self.my_model.Pacman._position[0]+1, self.my_model.Pacman._position[1], 2)

    def _set_controls(self):
        self.my_view._root.bind("w", lambda event: self._update_pacman_position("w"))
        self.my_view._root.bind("a", lambda event: self._update_pacman_position("a"))
        self.my_view._root.bind("s", lambda event: self._update_pacman_position("s"))
        self.my_view._root.bind("d", lambda event: self._update_pacman_position("d"))