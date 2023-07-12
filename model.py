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
            return r, c, gamePiece._ghost_pinky_home # ghost house color
        elif (self._current_level[r][c] == "4"):
            return r, c, gamePiece._ghost_blinky_home # ghost house color
        elif (self._current_level[r][c] == "5"):
            return r, c, gamePiece._ghost_clyde_home # ghost house color
        elif (self._current_level[r][c] == "6"):
            return r, c, gamePiece._ghost_inky_home # ghost house color
        
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

###################################PACMAN#######################################
    def _updated_position_of_pacman(self):
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

    def _distance_between_positions(self,x1, y1, x2, y2):
        #x - row
        #y - column
        distance = math.dist([x1, y1], [x2, y2])
        print(distance)
        return distance

    def _determine_direction_to_move_ghost(self, mode):
        
        if mode == 0: #scatter state
            for i in range(len(self.Ghosts)):
                #check which move is the right move to make, up, down, left, right
                #check the 4 directions, if wall, or backwards remove the options of moving in that direction

                if self.Ghosts[i]._direction == Direction._up:
                    #cannot be down, check if LEFT side and RIGHT side for a wall
                    leftside = self._scan_direction[self.Ghosts[i]._position[0],self.Ghosts[i]._position[1] - 1 ] 
                    rightside = self._scan_direction[self.Ghosts[i]._position[0],self.Ghosts[i]._position[1] + 1 ] 

                    #compare which move to make 
                    if leftside != gamePiece._path:
                        if rightside != gamePiece._path:
                            self._move_ghost(self.Ghosts[i], Direction._up)
                        else:
                            self._move_ghost(self.Ghosts[i], Direction._right)
                    else:
                        if rightside != gamePiece._path:
                            self._move_ghost(self.Ghosts[i], Direction._left)
                        else:
                            #check the distance between the two moves, left and right
                            leftdistance = self._distance_between_positions(self.Ghosts[i]._position[0], self.Ghosts[i]._position[1]-1, self.Ghosts[i]._scatter_target[0], self.ghosts[i]._scatter_target[1])
                            rightdistance = self._distance_between_positions(self.Ghosts[i]._position[0], self.Ghosts[i]._position[1]+1, self.Ghosts[i]._scatter_target[0], self.ghosts[i]._scatter_target[1])

                            if leftdistance < rightdistance:
                                self._move_ghost(self.Ghosts[i], Direction._left)
                            elif rightdistance < leftdistance:
                                self._move_ghost(self.Ghosts[i], Direction._right)
                            elif leftdistance == rightdistance : 
                                self._move_ghost (self.Ghosts[i], Direction._left)
                            else:
                                pass

                if self.Ghosts[i]._direction == Direction._down:
                    #cannot be UP, check if LEFT side and RIGHT side for a wall
                    leftside = self._scan_direction[self.Ghosts[i]._position[0],self.Ghosts[i]._position[1] - 1 ] 
                    rightside = self._scan_direction[self.Ghosts[i]._position[0],self.Ghosts[i]._position[1] + 1 ] 

                    #compare which move to make 
                    if leftside != gamePiece._path:
                        if rightside != gamePiece._path:
                            self._move_ghost(self.Ghosts[i], Direction._down)
                        else:
                            self._move_ghost(self.Ghosts[i], Direction._right)
                    else:
                        if rightside != gamePiece._path:
                            self._move_ghost(self.Ghosts[i], Direction._left)
                        else:
                            #check the distance between the two moves, LEFT and RIGHT
                            leftdistance = self._distance_between_positions(self.Ghosts[i]._position[0], self.Ghosts[i]._position[1]-1, self.Ghosts[i]._scatter_target[0], self.ghosts[i]._scatter_target[1])
                            rightdistance = self._distance_between_positions(self.Ghosts[i]._position[0], self.Ghosts[i]._position[1]+1, self.Ghosts[i]._scatter_target[0], self.ghosts[i]._scatter_target[1])

                            if leftdistance < rightdistance:
                                self._move_ghost(self.Ghosts[i], Direction._left)
                            elif rightdistance < leftdistance:
                                self._move_ghost(self.Ghosts[i], Direction._right)
                            elif leftdistance == rightdistance : 
                                self._move_ghost (self.Ghosts[i], Direction._left)
                            else:
                                pass

                if self.Ghosts[i]._direction == Direction._left:
                    #cannot be right, check if UP side and DOWN side for a wall
                    upside = self._scan_direction[self.Ghosts[i]._position[0]-1,self.Ghosts[i]._position[1]] 
                    downside = self._scan_direction[self.Ghosts[i]._position[0]+1,self.Ghosts[i]._position[1]] 

                    #compare which move to make 
                    if upside != gamePiece._path:
                        if downside != gamePiece._path:
                            self._move_ghost(self.Ghosts[i], Direction._left)
                        else:
                            self._move_ghost(self.Ghosts[i], Direction._down)
                    else:
                        if downside != gamePiece._path:
                            self._move_ghost(self.Ghosts[i], Direction._up)
                        else:
                            #check the distance between the two moves, left and right
                            updistance = self._distance_between_positions(self.Ghosts[i]._position[0]-1, self.Ghosts[i]._position[1], self.Ghosts[i]._scatter_target[0], self.ghosts[i]._scatter_target[1])
                            downdistance = self._distance_between_positions(self.Ghosts[i]._position[0]+1, self.Ghosts[i]._position[1], self.Ghosts[i]._scatter_target[0], self.ghosts[i]._scatter_target[1])

                            if updistance < downdistance:
                                self._move_ghost(self.Ghosts[i], Direction._up)
                            elif downdistance < updistance:
                                self._move_ghost(self.Ghosts[i], Direction._down)
                            elif updistance == downdistance : 
                                self._move_ghost (self.Ghosts[i], Direction._up)
                            else:
                                pass

                if self.Ghosts[i]._direction == Direction._right:
                    #cannot be left, check if UP side and DOWN side for a wall
                    upside = self._scan_direction[self.Ghosts[i]._position[0]-1,self.Ghosts[i]._position[1]] 
                    downside = self._scan_direction[self.Ghosts[i]._position[0]+1,self.Ghosts[i]._position[1]] 

                    #compare which move to make 
                    if upside != gamePiece._path:
                        if downside != gamePiece._path:
                            self._move_ghost(self.Ghosts[i], Direction._right)
                        else:
                            self._move_ghost(self.Ghosts[i], Direction._down)
                    else:
                        if downside != gamePiece._path:
                            self._move_ghost(self.Ghosts[i], Direction._up)
                        else:
                            #check the distance between the two moves, left and right
                            updistance = self._distance_between_positions(self.Ghosts[i]._position[0]-1, self.Ghosts[i]._position[1], self.Ghosts[i]._scatter_target[0], self.ghosts[i]._scatter_target[1])
                            downdistance = self._distance_between_positions(self.Ghosts[i]._position[0]+1, self.Ghosts[i]._position[1], self.Ghosts[i]._scatter_target[0], self.ghosts[i]._scatter_target[1])

                            if updistance < downdistance:
                                self._move_ghost(self.Ghosts[i], Direction._up)
                            elif downdistance < updistance:
                                self._move_ghost(self.Ghosts[i], Direction._down)
                            elif updistance == downdistance : 
                                self._move_ghost (self.Ghosts[i], Direction._up)
                            else:
                                pass
                            
        elif mode == 1: #chase

            for i in range(len(self.Ghosts)):
                #check which move is the right move to make, up, down, left, right
                #check the 4 directions, if wall, or backwards remove the options of moving in that direction

                if self.Ghosts[i]._direction == Direction._up:
                    #cannot be down, check if LEFT side and RIGHT side for a wall
                    leftside = self._scan_direction[self.Ghosts[i]._position[0],self.Ghosts[i]._position[1] - 1 ] 
                    rightside = self._scan_direction[self.Ghosts[i]._position[0],self.Ghosts[i]._position[1] + 1 ] 

                    #compare which move to make 
                    if leftside != gamePiece._path:
                        if rightside != gamePiece._path:
                            self._move_ghost(self.Ghosts[i], Direction._up)
                        else:
                            self._move_ghost(self.Ghosts[i], Direction._right)
                    else:
                        if rightside != gamePiece._path:
                            self._move_ghost(self.Ghosts[i], Direction._left)
                        else:
                            #check the distance between the two moves, left and right
                            leftdistance = self._distance_between_positions(self.Ghosts[i]._position[0], self.Ghosts[i]._position[1]-1, self.Pacman._position[0], self.Pacman._position[1])
                            rightdistance = self._distance_between_positions(self.Ghosts[i]._position[0], self.Ghosts[i]._position[1]+1, self.Pacman._position[0], self.Pacman._position[1])

                            if leftdistance < rightdistance:
                                self._move_ghost(self.Ghosts[i], Direction._left)
                            elif rightdistance < leftdistance:
                                self._move_ghost(self.Ghosts[i], Direction._right)
                            elif leftdistance == rightdistance : 
                                self._move_ghost (self.Ghosts[i], Direction._left)
                            else:
                                pass

                if self.Ghosts[i]._direction == Direction._down:
                    #cannot be UP, check if LEFT side and RIGHT side for a wall
                    leftside = self._scan_direction[self.Ghosts[i]._position[0],self.Ghosts[i]._position[1] - 1 ] 
                    rightside = self._scan_direction[self.Ghosts[i]._position[0],self.Ghosts[i]._position[1] + 1 ] 

                    #compare which move to make 
                    if leftside != gamePiece._path:
                        if rightside != gamePiece._path:
                            self._move_ghost(self.Ghosts[i], Direction._down)
                        else:
                            self._move_ghost(self.Ghosts[i], Direction._right)
                    else:
                        if rightside != gamePiece._path:
                            self._move_ghost(self.Ghosts[i], Direction._left)
                        else:
                            #check the distance between the two moves, LEFT and RIGHT
                            leftdistance = self._distance_between_positions(self.Ghosts[i]._position[0], self.Ghosts[i]._position[1]-1, self.Pacman._position[0], self.Pacman._position[1])
                            rightdistance = self._distance_between_positions(self.Ghosts[i]._position[0], self.Ghosts[i]._position[1]+1, self.Pacman._position[0], self.Pacman._position[1])

                            if leftdistance < rightdistance:
                                self._move_ghost(self.Ghosts[i], Direction._left)
                            elif rightdistance < leftdistance:
                                self._move_ghost(self.Ghosts[i], Direction._right)
                            elif leftdistance == rightdistance : 
                                self._move_ghost (self.Ghosts[i], Direction._left)
                            else:
                                pass

                if self.Ghosts[i]._direction == Direction._left:
                    #cannot be right, check if UP side and DOWN side for a wall
                    upside = self._scan_direction[self.Ghosts[i]._position[0]-1,self.Ghosts[i]._position[1]] 
                    downside = self._scan_direction[self.Ghosts[i]._position[0]+1,self.Ghosts[i]._position[1]] 

                    #compare which move to make 
                    if upside != gamePiece._path:
                        if downside != gamePiece._path:
                            self._move_ghost(self.Ghosts[i], Direction._left)
                        else:
                            self._move_ghost(self.Ghosts[i], Direction._down)
                    else:
                        if downside != gamePiece._path:
                            self._move_ghost(self.Ghosts[i], Direction._up)
                        else:
                            #check the distance between the two moves, left and right
                            updistance = self._distance_between_positions(self.Ghosts[i]._position[0]-1, self.Ghosts[i]._position[1], self.Pacman._position[0], self.Pacman._position[1])
                            downdistance = self._distance_between_positions(self.Ghosts[i]._position[0]+1, self.Ghosts[i]._position[1], self.Pacman._position[0], self.Pacman._position[1])

                            if updistance < downdistance:
                                self._move_ghost(self.Ghosts[i], Direction._up)
                            elif downdistance < updistance:
                                self._move_ghost(self.Ghosts[i], Direction._down)
                            elif updistance == downdistance : 
                                self._move_ghost (self.Ghosts[i], Direction._up)
                            else:
                                pass

                if self.Ghosts[i]._direction == Direction._right:
                    #cannot be left, check if UP side and DOWN side for a wall
                    upside = self._scan_direction[self.Ghosts[i]._position[0]-1,self.Ghosts[i]._position[1]] 
                    downside = self._scan_direction[self.Ghosts[i]._position[0]+1,self.Ghosts[i]._position[1]] 

                    #compare which move to make 
                    if upside != gamePiece._path:
                        if downside != gamePiece._path:
                            self._move_ghost(self.Ghosts[i], Direction._right)
                        else:
                            self._move_ghost(self.Ghosts[i], Direction._down)
                    else:
                        if downside != gamePiece._path:
                            self._move_ghost(self.Ghosts[i], Direction._up)
                        else:
                            #check the distance between the two moves, left and right
                            updistance = self._distance_between_positions(self.Ghosts[i]._position[0]-1, self.Ghosts[i]._position[1], self.Pacman._position[0], self.Pacman._position[1])
                            downdistance = self._distance_between_positions(self.Ghosts[i]._position[0]+1, self.Ghosts[i]._position[1], self.Pacman._position[0], self.Pacman._position[1])

                            if updistance < downdistance:
                                self._move_ghost(self.Ghosts[i], Direction._up)
                            elif downdistance < updistance:
                                self._move_ghost(self.Ghosts[i], Direction._down)
                            elif updistance == downdistance : 
                                self._move_ghost (self.Ghosts[i], Direction._up)
                            else:
                                pass
            
    def _move_ghost(self, ghost_obj, direction):
        pass