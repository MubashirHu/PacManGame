#This file contains the build of the GUI
from tkinter import *
from src.ghost import *
from src.pacman import *
from src.maze import *
class View:

    def __init__(self):

        #GUI window
        self._root = Tk()
        self._canvas = None 

        #objects
        self.PacmanMaze = Maze()
        self.Pacman = PacMan()
        self.GhostBlinky = Ghost("red")        
        self.GhostPinky = Ghost("pink")
        self.GhostInky = Ghost("cyan")
        self.GhostClyde = Ghost("orange")

        #data storage
        
    def _draw_board(self):
        for i in range(self.PacmanMaze._rows):
            for j in range(self.PacmanMaze._columns):
                if self._current_level[i][j] == 1:
                    #print blue walls
                    x0 = i * self._square_size
                    y0 = j * self._square_size
                    x1 = x0 + self._square_size
                    y1 = y0 + self._square_size
                    self.GameWindow._canvas.create_rectangle(x0, y0, x1, y1, fill='green')
                
                elif self._current_level[i][j] == 0:
                    #print black walk area
                    x0 = i * self._square_size
                    y0 = j * self._square_size
                    x1 = x0 + self._square_size
                    y1 = y0 + self._square_size
                    self.GameWindow._canvas.create_rectangle(x0, y0, x1, y1, fill='green')

                else: print("ERROR in drawing board")
                
                print(self._current_level[i][j])

    def _move_pacman(self):
        pass

    def _move_ghost(self):
        pass

    def _update_score(self):
        pass

    def _game_over(self):
        pass

    def _restart(self):
        pass

    def _quit(self):
        pass

    def _set_level(self, level):
        if level == 1:
            self._current_level = self.PacmanMaze._get_level(1)
        elif level == 2:
            self._current_level = self.PacmanMaze._get_level(2)
        elif level == 3:
            self._current_level = self.PacmanMaze._get_level(3)

    def _initialize(self):
        #self._root.configure(bg = 'black')
        self._root.title('PacMan Game')
        self._root.geometry('1000x1000')

        self._canvas = Canvas(self._root, bg='white')
        self._canvas.pack()

view = View()
view._initialize()
view._draw_board()

view._root.mainloop()