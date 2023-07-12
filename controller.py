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

        self.my_view._root.bind("w", lambda event: self._get_user_input("w"))
        self.my_view._root.bind("a", lambda event: self._get_user_input("a"))
        self.my_view._root.bind("s", lambda event: self._get_user_input("s"))
        self.my_view._root.bind("d", lambda event: self._get_user_input("d"))

        self._game_started = False
        self._scheduling_speed = 400
        self._last_key_pressed = None
        self._last_direction = None
        self._pacman_update_event = 1


    def _get_user_input(self, direction):
        if(direction == "w"):
            self._game_started = True
            if self._last_key_pressed == "w" and self._last_direction == Direction._up:
                pass
            else:
                self.my_model.Pacman._movement_direction = Direction._up
                self._last_key_pressed = "w"
                self._update_pacman_position()

        if(direction == "a"):
            self._game_started = True            
            if self. _last_key_pressed == "a" and self._last_direction == Direction._left:
                pass
            else:
                self._last_key_pressed = "a"
                self.my_model.Pacman._movement_direction = Direction._left
                self._update_pacman_position()

        if(direction == "s"):
            self._game_started = True
            if self._last_key_pressed == "s" and self._last_direction == Direction._down:
                pass
            else:
                self._last_key_pressed = "s"
                self.my_model.Pacman._movement_direction = Direction._down
                self._update_pacman_position()

        if(direction == "d"):
            self._game_started = True
            if self._last_key_pressed == "d" and self._last_direction == Direction._right :
                pass
            else:
                self._last_key_pressed = "d"
                self.my_model.Pacman._movement_direction = Direction._right   
                self._update_pacman_position()

    def _initialize_model_and_view(self):
        if self.my_model._initialize():
            if self.my_view._initialize():
                print("Both view and model have been initialized...")

    def _draw_maze(self):
        for r in range(self.my_model.Map._rows):
            for c in range(self.my_model.Map._columns):
                location_and_shape = self.my_model._check_gamepiece(0, r, c)       
                self.my_view._draw_shape(location_and_shape[0], location_and_shape[1], location_and_shape[2])     
        
        self.my_view._draw_shape(self.my_model.Pacman._position[0], self.my_model.Pacman._position[1], gamePiece._pacman)

        for i in range (len(self.my_model.Ghosts)):
            self.my_view._draw_ghost(self.my_model.Ghosts[i]._position[0], self.my_model.Ghosts[i]._position[1], self.my_model.Ghosts[i])

    def _update_pacman_position(self):
        if self._pacman_update_event is not None:
            self.my_view._root.after_cancel(self._pacman_update_event)

        if self.my_model.Pacman._movement_direction != Direction._idle:
            if self.my_model._updated_position_of_pacman():
                self.my_view._updated_position_of_pacman(self.my_model.Pacman._position[0], self.my_model.Pacman._position[1])
                self._display_coordinates()
            else:
                self.my_model.Pacman._movement_direction = self._last_direction

        self._pacman_update_event = self.my_view._root.after(self._scheduling_speed, self._update_pacman_position)  # Schedule
        return 1
    
    def _display_coordinates(self):
        self.my_view._display_pacman_position_text(self.my_model.Pacman._position[0],self.my_model.Pacman._position[1], self.my_model.Pacman._state)
        
        for i in range(len(self.my_model.Ghosts)):
            self.my_view._display_ghost_position_text(self.my_model.Ghosts[i])

    #TODO
    def _update_ghosts_position(self):
        pass
 
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')