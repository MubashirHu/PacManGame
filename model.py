#This file contains the logic of the pacman gameThe model component represents the data and business logic of your game. In a Pac-Man game, this would include information about the game state, such as the position of Pac-Man and the ghosts, the state of the maze, the score, and the number of lives remaining. Here's how you can build the model component:
from src.ghost import *
from src.pacman import *
from src.maze import *
from src.util import *
import math

class Model:
    def __init__(self):

        #objects
        self.Map = Maze()
        self.Pacman = PacMan()
        self.Ghosts = []

        self.GhostBlinky = Ghost("Blinky", "red", Direction._up)        
        self.GhostPinky = Ghost("Pinky", "pink", Direction._up)
        self.GhostInky = Ghost("Inky",  "cyan", Direction._up)
        self.GhostClyde = Ghost("Clyde","orange", Direction._up)

        self.Ghosts.append(self.GhostPinky)
        self.Ghosts.append(self.GhostBlinky)
        self.Ghosts.append(self.GhostClyde)
        self.Ghosts.append(self.GhostInky)
        
        #data
        self._current_level = []

    def _initialize(self):

        #initialize maze
        self._current_level = self.Map._get_level(1)

        #initialize pacman
        self.Pacman._get_starting_position(self.Map, self._current_level)

        #initialize ghosts
        for i in range (len(self.Ghosts)):
            self.Ghosts[i]._get_starting_position(self.Ghosts[i], self.Map, self._current_level)
            self.Ghosts[i]._set_scatter_target(self.Ghosts[i]._name)

        return 1

    def _scan_direction(self, obj = 0, r=0, c=0, direction = Direction._idle):

        if direction == Direction._up:
            r = obj.row-1
            c = obj.col
        elif direction == Direction._down:
            r = obj.row+1
            c = obj.col
        elif direction == Direction._left:
            r = obj.row
            c = obj.col-1
        elif direction == Direction._right:
            r = obj.row
            c = obj.col+1
        else:
            pass

        if(self._current_level[r][c] == "1"):
            return r, c, gamePiece._wall # wall
        elif (self._current_level[r][c] == "0"):
            return r, c, gamePiece._path # path
        elif (self._current_level[r][c] == "2"):
            return r, c, gamePiece._ghost_house_path # ghost house color
        elif (self._current_level[r][c] == "3"):
            return r, c, gamePiece._pinky # ghost house color
        elif (self._current_level[r][c] == "4"):
            return r, c, gamePiece._blinky # ghost house color
        elif (self._current_level[r][c] == "5"):
            return r, c, gamePiece._clyde # ghost house color
        elif (self._current_level[r][c] == "6"):
            return r, c, gamePiece._inky # ghost house color
        
###################################PACMAN#######################################
    def _is_move_valid_for_pacman(self, direction):
        if direction == Direction._up:
            scanned_obj = self._scan_direction(self.Pacman, self.Pacman.row, self.Pacman.col, direction)
            if scanned_obj[2] == gamePiece._path:
                return 1
            else:
                return 0
            
        elif direction == Direction._down:
            scanned_obj = self._scan_direction(self.Pacman, self.Pacman.row, self.Pacman.col, direction)
            if scanned_obj[2] == gamePiece._path:
                return 1
            else:
                return 0
            
        elif direction == Direction._left:
            scanned_obj = self._scan_direction(self.Pacman, self.Pacman.row, self.Pacman.col, direction)
            if scanned_obj[2] == gamePiece._path:
                return 1
            else:
                return 0
            
        elif direction == Direction._right:
            scanned_obj = self._scan_direction(self.Pacman, self.Pacman.row, self.Pacman.col, direction)
            if scanned_obj[2] == gamePiece._path:
                return 1
            else:
                return 0  
        else:
            print("Not part of the controls")
            return 0

    def _update_position_of_pacman(self):
        if(self.Pacman._movement_direction == Direction._up):
            if(self._is_move_valid_for_pacman(Direction._up)):
                self.Pacman.row -= 1
                self._last_direction = Direction._up
                return 1
            else:
                return 0
                
        elif (self.Pacman._movement_direction == Direction._down):
            if(self._is_move_valid_for_pacman(Direction._down)):
                self.Pacman.row += 1
                self._last_direction = Direction._down
                return 1
            else:
                return 0
            
        elif (self.Pacman._movement_direction == Direction._left):
            if(self._is_move_valid_for_pacman(Direction._left)):
                self.Pacman.col -= 1
                self._last_direction = Direction._left
                return 1
            else:
                return 0
            
        elif (self.Pacman._movement_direction == Direction._right):
            if(self._is_move_valid_for_pacman(Direction._right)):
                self.Pacman.col += 1
                self._last_direction = Direction._right
                return 1
            else:
                return 0
        elif (self.Pacman._movement_direction == Direction._idle):
            return 0

###################################GHOST#######################################

    def _move_ghost(self, ghost_obj, direction):
        if direction == Direction._up:
            ghost_obj.row -= 1
        elif direction == Direction._down:
            ghost_obj.row += 1
        elif direction == Direction._left:
            ghost_obj.col -= 1
        elif direction == Direction._right:
            ghost_obj.col += 1
        else:
            pass
    
    def _distance_between_ghost_and_target(self, ghost_obj, direction=Direction._idle ):

        #set the target coordinate based on state
        if ghost_obj._state == ghostState._scatter:
            x2 = ghost_obj._scatter_target[0]
            y2 = ghost_obj._scatter_target[1]
        elif ghost_obj._state == ghostState._chase:
            x2 = self.Pacman.row
            y2 = self.Pacman.col

        #which direction around the ghost should be selected
        if direction == Direction._left:
            x1 = ghost_obj.row
            y1 = ghost_obj.col-1
    
        elif direction == Direction._right:
            x1 = ghost_obj.row
            y1 = ghost_obj.col+1

        elif direction == Direction._up:
            x1 = ghost_obj.row-1
            y1 = ghost_obj.col
            
        elif direction == Direction._down:
            x1 = ghost_obj.row
            y1 = ghost_obj.col-1
        else:
            x1 = ghost_obj.row
            y1 = ghost_obj.col

        distance = math.dist([x1, y1], [x2, y2])
        print(distance)
        return distance
    
    def _determine_least_direction(self, value1, value2, direction=Direction._idle):
        if direction == Direction._up or direction == Direction._down:
            if value1 < value2:
                return Direction._left
            elif value2 < value1:
                return Direction._right
            elif value1 == value2 : 
                return direction
            else:
                pass
        elif direction == Direction._left or direction == Direction._right:
            if value1 < value2:
                return Direction._up
            elif value2 < value1:
                return Direction._down
            elif value1 == value2 : 
                return direction
            else:
                pass

        else:
            pass
         
    def _update_position_of_ghost(self, ghost_obj):
        #up down
        #left right
    
        if ghost_obj._direction == Direction._up or ghost_obj._direction == Direction._down:
            
            left = self._scan_direction(ghost_obj, ghost_obj.row, ghost_obj.col, Direction._left)
            right = self._scan_direction(ghost_obj, ghost_obj.row, ghost_obj.col, Direction._right)
            
            if left != gamePiece._path or left != gamePiece._ghost_house:
                if right != gamePiece._path or right != gamePiece._ghost_house:
                    self._move_ghost(ghost_obj, ghost_obj._direction)
                else:
                    ghost_obj._direction = Direction._right
                    self._move_ghost(ghost_obj, Direction._right)
            else:
                if right != gamePiece._path or right != gamePiece._ghost_house:
                    ghost_obj._direction = Direction._left
                    self._move_ghost(ghost_obj, Direction._left)
                else:
                    #check the distance between the two moves, left and right
                    leftdistance = self._distance_between_ghost_and_target(ghost_obj, Direction._left)
                    rightdistance = self._distance_between_ghost_and_target(ghost_obj, Direction._right)

                    least_linear_direction = self._determine_least_direction(leftdistance, rightdistance, ghost_obj._direction)
                    ghost_obj._direction = least_linear_direction
                    self._move_ghost(ghost_obj, least_linear_direction)
                    
            return 1

        elif ghost_obj._direction == Direction._left or ghost_obj._direction == Direction._right:

            up = self._scan_direction(ghost_obj, ghost_obj.row, ghost_obj.col, Direction._up)
            down = self._scan_direction(ghost_obj, ghost_obj.row, ghost_obj.col, Direction._down)
            
            if up != gamePiece._path or up != gamePiece._ghost_house:
                if down != gamePiece._path or down != gamePiece._ghost_house:
                    self._move_ghost(ghost_obj, ghost_obj._direction)
                else:
                    ghost_obj._direction = Direction._down
                    self._move_ghost(ghost_obj, Direction._down)
            else:
                if down != gamePiece._path or down != gamePiece._ghost_house:
                    ghost_obj._direction = Direction._up
                    self._move_ghost(ghost_obj, Direction._up)
                else:
                    #check the distance between the two moves, up and down
                    updistance = self._distance_between_ghost_and_target(ghost_obj, Direction._up)
                    downdistance = self._distance_between_ghost_and_target(ghost_obj, Direction._down)

                    least_linear_direction = self._determine_least_direction(updistance, downdistance, ghost_obj._direction)
                    ghost_obj._direction = least_linear_direction
                    self._move_ghost(ghost_obj, least_linear_direction)
                    return 1
            
        else:
            print("ERROR: ghosts are in idle")
        

            
    