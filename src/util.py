from enum import Enum
class Direction(Enum):
    _up = 1
    _down = 2
    _left = 3
    _right = 4
    _idle = 5

class Map(Enum):
    _pacman = 1
    _wall = 2
    _path = 3
    _ghost = 4