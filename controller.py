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

    def _update_position_of_pacman(self):
        if(self.my_model._pacman_movement_direction == Direction._up):
            _move_valid = self.my_model._is_move_valid(Direction._up)
            if(_move_valid):
                self.my_view._draw_shape(self.my_model.Pacman._position[0], self.my_model.Pacman._position[1], 2)
            else:
                self.my_model._pacman_movement_direction._idle

        elif (self.my_model._pacman_movement_direction == Direction._down):
            _move_valid = self.my_model._is_move_valid(Direction._down)
            if(_move_valid):
                self.my_view._draw_shape(self.my_model.Pacman._position[0], self.my_model.Pacman._position[1], 2)
            else:
                self.my_model._pacman_movement_direction._idle
        elif (self.my_model._pacman_movement_direction == Direction._left):
            _move_valid = self.my_model._is_move_valid(Direction._left)
            if(_move_valid):
                self.my_view._draw_shape(self.my_model.Pacman._position[0], self.my_model.Pacman._position[1], 2)
            else:
                self.my_model._pacman_movement_direction._idle
        elif (self.my_model._pacman_movement_direction == Direction._right):
            _move_valid = self.my_model._is_move_valid(Direction._right)
            if(_move_valid):
                self.my_view._draw_shape(self.my_model.Pacman._position[0], self.my_model.Pacman._position[1], 2)
            else:
                self.my_model._pacman_movement_direction._idle
        elif (self.my_model._pacman_movement_direction == Direction._idle):
            _move_valid = self.my_model._is_move_valid(Direction._idle)
            if(_move_valid):
                self.my_view._draw_shape(self.my_model.Pacman._position[0], self.my_model.Pacman._position[1], 2)
            else:
                self.my_model._pacman_movement_direction._idle
        
    def _get_user_input(self, direction):
        if(direction == "w"):
            self.my_model._pacman_movement_direction = Direction._up
            self._update_position_of_pacman()
        if(direction == "a"):
            self.my_model._pacman_movement_direction = Direction._left
            self._update_position_of_pacman()
        if(direction == "s"):
            self.my_model._pacman_movement_direction = Direction._down
            self._update_position_of_pacman()
        if(direction == "d"):
            self.my_model._pacman_movement_direction = Direction._right
            self._update_position_of_pacman()

        #self.clear()
        #print coordinates
        for i in range(len(self.my_model.Pacman._position)):
            print(self.my_model.Pacman._position[i])

        #print row and column count
        self.my_model.Map._get_number_of_rows
        self.my_model.Map._get_number_of_columns            

    def _set_controls(self):
        self.my_view._root.bind("w", lambda event: self._get_user_input("w"))
        self.my_view._root.bind("a", lambda event: self._get_user_input("a"))
        self.my_view._root.bind("s", lambda event: self._get_user_input("s"))
        self.my_view._root.bind("d", lambda event: self._get_user_input("d"))

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')