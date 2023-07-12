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

    ##Initialization
    def _initialize_model_and_view(self):
        if self.my_model._initialize():
            if self.my_view._initialize():
                print("Both view and model have been initialized...")
            
        self._draw_maze_pacman_ghosts()
        self._display_coordinates()    

    def _draw_maze_pacman_ghosts(self):
        
        #draw the walls and path
        for r in range(self.my_model.Map._rows):
            for c in range(self.my_model.Map._columns):
                tmp = self.my_model._scan_direction(None, r, c, None)       
                self.my_view._draw_shape(tmp[0], tmp[1], tmp[2])     
        
        #draw pacman
        self.my_view._draw_shape(self.my_model.Pacman.row, self.my_model.Pacman.col, gamePiece._pacman)

        #draw ghosts 
        for i in range (len(self.my_model.Ghosts)):
            self.my_view._draw_ghost(self.my_model.Ghosts[i].row, self.my_model.Ghosts[i].col, self.my_model.Ghosts[i])

    def _display_coordinates(self):
        self.my_view._display_pacman_position_text(self.my_model.Pacman.row,self.my_model.Pacman.col, self.my_model.Pacman._state)
        
        for i in range(len(self.my_model.Ghosts)):
            self.my_view._display_ghost_position_text(self.my_model.Ghosts[i])

    #main loop
    def _get_user_input(self, direction):
        if(direction == "w"):
            self._game_started = True
            if self._last_key_pressed == "w" and self._last_direction == Direction._up:
                pass
            else:
                self.my_model.Pacman._movement_direction = Direction._up
                self._last_key_pressed = "w"
                self._move_pacman_in_pressed_direction()

        if(direction == "a"):
            self._game_started = True            
            if self. _last_key_pressed == "a" and self._last_direction == Direction._left:
                pass
            else:
                self._last_key_pressed = "a"
                self.my_model.Pacman._movement_direction = Direction._left
                self._move_pacman_in_pressed_direction()

        if(direction == "s"):
            self._game_started = True
            if self._last_key_pressed == "s" and self._last_direction == Direction._down:
                pass
            else:
                self._last_key_pressed = "s"
                self.my_model.Pacman._movement_direction = Direction._down
                self._move_pacman_in_pressed_direction()

        if(direction == "d"):
            self._game_started = True
            if self._last_key_pressed == "d" and self._last_direction == Direction._right :
                pass
            else:
                self._last_key_pressed = "d"
                self.my_model.Pacman._movement_direction = Direction._right   
                self._move_pacman_in_pressed_direction()
    
    def _move_pacman_in_pressed_direction(self):
        if self._pacman_update_event is not None:
            self.my_view._root.after_cancel(self._pacman_update_event)

        if self.my_model.Pacman._movement_direction != Direction._idle:
            if self.my_model._update_position_of_pacman():
                self.my_view._update_position_of_pacman(self.my_model.Pacman.row, self.my_model.Pacman.col)
            else:
                self.my_model.Pacman._movement_direction = self._last_direction

        self._display_coordinates()
        self._pacman_update_event = self.my_view._root.after(self._scheduling_speed, self._move_pacman_in_pressed_direction)  # Schedule
        return 1
    
    #TODO working on proggress
    def ghost_ai(self):

        for i in range (len(self.my_model.Ghosts)):

            if self._ghost_update_event is not None:
                self.my_view._root.after_cancel(self._ghost_update_event)

            if self._game_started:

                if self.my_model._update_position_of_ghost(self.my_model.Ghosts[i], self.my_model.Ghosts[i]._direction):
                    self.my_view._update_position_of_ghost(self.my_model.Ghosts[i].row, self.my_model.Ghosts[i].col)
            
        self._display_coordinates()
        self._ghost_update_event = self.my_view._root.after(self._scheduling_speed, self.ghost_ai)  # Schedule
        return 1
     
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')