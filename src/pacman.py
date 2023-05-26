from src.util import *
class PacMan:
    def __init__(self):
        self._position = []
        self._movement_direction = Direction._idle
        self._lives = 0
        self._current_score = 0
        self._speed = 0
        self._status = 0
        self._power_up_timer = 0
        self._power_up_duration = 0
        self._power_up_score = 0
        
    #setters
    def _set_position(self, row, column):
        self._position = (row,column)

    def _set_direction(self, direction):
        self._movement_direction = direction

    def _set_lives(self, lives):
        self._lives = lives
        
    def _set_currentScore(self, score):
        self._currentScore = score

    def _set_speed(self, speed):
        self._speed = speed

    def _set_status(self, status):
        self._status = status
        
    def _set_power_up_timer(self, timer):
        self._power_up_timer = timer

    def _set_power_up_duration(self, duration):
        self._power_up_duration = duration

    def _set_power_up_score(self, score):
        self._set_power_up_score

    #getters
    def _get_position(self):
        return self._position
    
    def _get_direction(self):
        return self._direction
    
    def _get_lives(self):
        return self._lives
    
    def _get_currentScore(self):
        return self._current_score
    
    def _get_speed(self):
        return self._speed
    
    def _get_status(self):
        return self._status
    
    def _get_power_up_timer(self):
        return self._power_up_timer
    
    def _get_power_up_duration(self):
        return self._power_up_duration
    
    def _get_power_up_score(self):
        return self._power_up_score
    
    def _get_pacman_starting_position_from_current_level(self, map_obj, _current_level):
        

        x = int(map_obj._rows/2)
        y = int(map_obj._columns/2)
        
        if _current_level[x][y] == "1":
            
            if([x + 1][y + 1] != "1"): # bottom right
                self._position.append(x+1)
                self._position.append(y+1)
            elif ([x + 1][y - 1] != "1"): # bottom left
                self._position.append(x+1)
                self._position.append(y-1)
            elif ([x - 1][y + 1] != "1"): # top right
                self._position.append(x-1)
                self._position.append(y+1)
            elif ([x - 1][y - 1] != "1"): #top left
                self._position.append(x-1) 
                self._position.append(y-1)
            else:
                print("ERROR: No starting position available")
                return False 
            return True
        else:
            self._position.append(x)
            self._position.append(y)
            return True
