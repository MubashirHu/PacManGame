from enum import Enum
class Direction(Enum):
    _up = 1
    _down = 2
    _left = 3
    _right = 4
    _idle = 5

class gamePiece(Enum):
    _none = 0
    _pacman = 1
    _wall = 2
    _path = 3
    _ghost_house = 4
    _ghost = 5
    _ghost_house_path = 6
    
    _ghost_inky_home = 7
    _ghost_pinky_home = 8
    _ghost_blinky_home = 9
    _ghost_clyde_home = 10

class ghostState(Enum):
    _scatter = 0
    _chase = 1
    _frightened = 2
    _eaten = 3

class pacmanState(Enum):
    _no_buff = 0
    _has_power_buff = 1
    _has_speed_buff = 2
    