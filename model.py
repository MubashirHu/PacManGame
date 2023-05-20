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

    def _move_pacman(self, direction):
        if direction == 'up':
            self.Pacman._position[1] += 1
        elif direction == 'down':
            self.Pacman._position[1] -= 1
        elif direction == 'right':
            self.Pacman._position[0] += 1
        elif direction == 'left':
            self.Pacman._position[0] -= 1
        else:
            print("ERROR in _move_pacman")

    def _check_for_walls_and_path(self, row, column):
        if(self._current_level[row][column] == "1"):
            return row, column, 1
        elif (self._current_level[row][column] == "0"):
            return row, column, 0

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