#This file contains the logic of the pacman gameThe model component represents the data and business logic of your game. In a Pac-Man game, this would include information about the game state, such as the position of Pac-Man and the ghosts, the state of the maze, the score, and the number of lives remaining. Here's how you can build the model component:
from src.ghost import *
from src.pacman import *
from src.maze import *
from src.util import *

class Model:
    def __init__(self):

        #objects
        self.Map = Maze()
        self.Pacman = PacMan()
        self.GhostBlinky = Ghost("red")        
        self.GhostPinky = Ghost("pink")
        self.GhostInky = Ghost("cyan")
        self.GhostClyde = Ghost("orange")

        #data
        self._current_level = []
        self._pacman_movement_direction = Direction._idle

    def _initialize(self):
        self._set_level(1)
        self.Pacman._get_pacman_starting_position_from_current_level(self.Map, self._current_level)
        
        return 1
        #add pacman
        
    def _set_level(self, level):
        if level == 1:
            self._current_level = self.Map._get_level(1)
        elif level == 2:
            self._current_level = self.Map._get_level(2)
        elif level == 3:
            self._current_level = self.Map._get_level(3)

    def _check_for_walls_and_path(self, row, column):
        if(self._current_level[row][column] == "1"):
            return row, column, 1
        elif (self._current_level[row][column] == "0"):
            return row, column, 0
        
    def _move_pacman_in_direction(self, direction):
        if direction == Direction._up :
            pass
        elif direction == Direction._down:
            pass
        elif direction == Direction._left:
            pass
        elif direction == Direction._right:
            pass
        elif direction == Direction._idle:
            pass

    def _is_move_valid(self, direction):
        if direction == Direction._up:
            self._pacman_movement_direction = Direction._up
            row = self.Pacman._position[0]-1
            column = self.Pacman._position[1]
            if self._current_level[row][column] == "0":
                self.Pacman._position[0] -= 1
                return 1
            elif self._current_level[row][column] == "1":
                self._pacman_movement_direction = Direction._idle
                return 0
        elif direction == Direction._left:
            self._pacman_movement_direction = Direction._left
            row = self.Pacman._position[0]
            column = self.Pacman._position[1]-1
            if self._current_level[row][column] == "0":
                self.Pacman._position[1] -= 1
                return 1
            elif self._current_level[row][column] == "1":
                self._pacman_movement_direction = Direction._idle
                return 0
            
        elif direction == Direction._down:
            row = self.Pacman._position[0]+1
            column = self.Pacman._position[1]
            if self._current_level[row][column] == "0":
                self.Pacman._position[0] += 1
                return 1
            elif self._current_level[row][column] == "1":
                self._pacman_movement_direction = Direction._idle
                return 0
            
        elif direction == Direction._right:
            row = self.Pacman._position[0]
            column = self.Pacman._position[1] +1
            if self._current_level[row][column] == "0":
                self.Pacman._position[1] += 1
                return 1
            elif self._current_level[row][column] == "1":
                self._pacman_movement_direction = Direction._idle
                return 0
            
        elif direction == Direction._idle:
            row = self.Pacman._position[0]
            column = self.Pacman._position[1]
            if self._current_level[row][column] == "0":
                return 1
            elif self._current_level[row][column] == "1":
                self._pacman_movement_direction = Direction._idle
                return 0  
        else:
            print("Not part of the controls")
            return 0
             

    def _move_ghost(self, obj):
        pass

    def _update_score(self):
        pass

    def _game_over(self):
        pass

    def _restart(self):
        pass

    def _quit(self):
        pass