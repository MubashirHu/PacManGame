#This file contains the build of the GUI
from tkinter import *
from ghost import *
from pacman import *
from maze import *

class PacmanGUI:

    
    
    def __init__(self):
        self._root = Tk()
        self._maze = maze()
        self._pacman = pacMan()
        self._ghost_blinky = ghost()        
        self._ghost_pinky = ghost()
        self._ghost_inky = ghost()
        self._ghost_clyde = ghost()

    def _display_game(self):
        pass





root = Tk()

root.mainloop()