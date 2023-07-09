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
        self.Ghosts = []

        self.GhostBlinky = Ghost("Blinky","red")        
        self.GhostPinky = Ghost("Pinky", "pink")
        self.GhostInky = Ghost("Inky", "cyan")
        self.GhostClyde = Ghost("Clyde","orange")

        self.Ghosts.append(self.GhostPinky)
        self.Ghosts.append(self.GhostBlinky)
        self.Ghosts.append(self.GhostClyde)
        self.Ghosts.append(self.GhostInky)
        
        #data
        self._current_level = []

    def _initialize(self):
        self._set_level(1)

        #set initial positions
        self.Pacman._get_pacman_starting_position_from_current_level(self.Map, self._current_level)

        for i in range (len(self.Ghosts)):
            self.Ghosts[i]._get_starting_position(self.Ghosts[i], self.Map, self._current_level)
        return 1
        
    def _set_level(self, level):
        if level == 1:
            self._current_level = self.Map._get_level(1)
        elif level == 2:
            self._current_level = self.Map._get_level(2)
        elif level == 3:
            self._current_level = self.Map._get_level(3)

    def _check_for_walls_and_pellet(self, row, column):
        if(self._current_level[row][column] == "1"):
            return row, column, gamePiece._wall # wall
        elif (self._current_level[row][column] == "0"):
            return row, column, gamePiece._pellet # path
        elif (self._current_level[row][column] == "2"):
            return row, column, gamePiece._ghost_house_path # ghost house color
        elif (self._current_level[row][column] == "3"):
            return row, column, gamePiece._ghost_pinky_home # ghost house color
        elif (self._current_level[row][column] == "4"):
            return row, column, gamePiece._ghost_blinky_home # ghost house color
        elif (self._current_level[row][column] == "5"):
            return row, column, gamePiece._ghost_clyde_home # ghost house color
        elif (self._current_level[row][column] == "6"):
            return row, column, gamePiece._ghost_inky_home # ghost house color
        
    def _is_move_valid(self, direction):
        if direction == Direction._up:
            row = self.Pacman._position[0]-1
            column = self.Pacman._position[1]
            if self._current_level[row][column] == "0":
                self.Pacman._position[0] -= 1
                return 1
            elif self._current_level[row][column] == "1":
                self.Pacman._movement_direction = Direction._idle
                return 0
            
        elif direction == Direction._left:
            row = self.Pacman._position[0]
            column = self.Pacman._position[1]-1
            if self._current_level[row][column] == "0":
                self.Pacman._position[1] -= 1
                return 1
            elif self._current_level[row][column] == "1":
                self.Pacman._movement_direction = Direction._idle
                return 0
            
        elif direction == Direction._down:
            row = self.Pacman._position[0]+1
            column = self.Pacman._position[1]
            if self._current_level[row][column] == "0":
                self.Pacman._position[0] += 1
                return 1
            elif self._current_level[row][column] == "1":
                self.Pacman._movement_direction = Direction._idle
                return 0
            
        elif direction == Direction._right:
            row = self.Pacman._position[0]
            column = self.Pacman._position[1] +1
            if self._current_level[row][column] == "0":
                self.Pacman._position[1] += 1
                return 1
            elif self._current_level[row][column] == "1":
                self.Pacman._movement_direction = Direction._idle
                return 0
            
        elif direction == Direction._idle:
            row = self.Pacman._position[0]
            column = self.Pacman._position[1]
            if self._current_level[row][column] == "0":
                return 1
            elif self._current_level[row][column] == "1":
                self.Pacman._movement_direction = Direction._idle
                return 0  
        else:
            print("Not part of the controls")
            return 0
        
    def _set_scatter_target_in_model(self):
        for i in range(len(self.Ghosts)):
            if self.Ghosts[i]._name == "Pinky":
                r = 0
                c = 0
            elif self.Ghosts[i]._name == "Blinky":
                r = 0
                c = 27
            elif self.Ghosts[i]._name == "Clyde":
                r = 26
                c = 0
            elif self.Ghosts[i]._name == "Inky":
                r = 26
                c = 27

            self.Ghosts[i]._set_scatter_target(r,c)

    def _move_ghost_towards_scatter_target(self, ghost_obj):
        pass

    def _update_score(self):
        pass

    def _game_over(self):
        pass

    def _restart(self):
        pass

    def _quit(self):
        pass