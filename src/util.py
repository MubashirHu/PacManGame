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
    _pellet = 3
    _ghost_house = 4
    _ghost = 5