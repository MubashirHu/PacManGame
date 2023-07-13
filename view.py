#This file contains the build of the GUI
from tkinter import *
from src.util import *
import time 
class View:

    def __init__(self):
        #GUI window
        self._root = Tk()
        self._canvas = None
        self._label = None
        self._shape_size = 21
        self._path_size = 21
        self._wall_color = "blue"
        self._path_color = "purple"
        self._pacman_color = "yellow"
        self._ghost_house_path_color = "green"
        self._ghost_house_base_color = "white"

    def _initialize(self):
        self._root.title('PacMan Game')
        self._root.geometry('1200x1000')

        self._canvas = Canvas(self._root, width=590, height=570, bg='black')
        self._canvas.grid(row=0, column=3)
        return 1
    
    def _draw_shape(self, col, row, shape, ghost_obj=None):

        if ghost_obj is not None:
            
            if (shape == gamePiece._ghost):
                if self._draw_ghost_in_position(ghost_obj):
                    return 1
                else:
                    return 0
            else:
                print("ERROR: Unidentified shape")
                return 0
        else:

            if (shape == gamePiece._path):
                if self.add_shape(self, row, col, self._path_size, gamePiece._path, self._path_color):
                    return 1
                else:
                    return 0
                
            elif(shape == gamePiece._wall):
                if self.add_shape(self, row, col, self._shape_size, gamePiece._wall, self._wall_color):
                    return 1
                else:
                    return 0
                
            elif(shape == gamePiece._pacman):
                if self._draw_pacman_in_position(row, col):
                    if self._eat_path_in_position(row, col):
                        return 1
                    else:
                        return 0
                else:
                    return 0
                
            elif(shape == gamePiece._ghost_house_path):
                if self.add_shape(self, row, col, self._shape_size, gamePiece._ghost_house, self._ghost_house_path_color):
                    return 1
                else:
                    print("ERROR: Unidentified shape")
                    return 0
            

    def _draw_pacman_in_position(self, row, col):
        self._canvas.delete(gamePiece._pacman)
        if self.add_shape(self, row, col, self._shape_size, gamePiece._pacman, self._pacman_color):
            return 1
        else:
            return 0
        
    def _draw_ghost_in_position(self, ghost_obj):
        if self.add_shape(self, ghost_obj.col, ghost_obj.row, self._shape_size, gamePiece._ghost, ghost_obj._color):
            return 1
        else:
            return 0
    
    def _eat_path_in_position(self, row, col):
        pellet_id = self._canvas.find_withtag(f"{row}_{col}")
        if pellet_id:
            self._canvas.delete(pellet_id)
            return 1
        else:
            return 0
        
    def add_shape(self, tk_obj, i,j, size, gamepiece, color):
        if gamepiece == gamePiece._pacman:
            x0 = i * size
            y0 = j * size 
            x1 = x0 + size 
            y1 = y0 + size 
            self._canvas.create_oval(x0, y0, x1, y1, tags= gamePiece._pacman, fill=color)
            return 1

        if gamepiece == gamePiece._path:
            x0 = i * size
            y0 = j * size
            x1 = x0 + size 
            y1 = y0 + size
            self._canvas.create_oval(x0, y0, x1, y1, tags= f"{i}_{j}", fill=color)
            return 1

        elif gamepiece == gamePiece._wall:
            x0 = i * size
            y0 = j * size
            x1 = x0 + size
            y1 = y0 + size
            self._canvas.create_rectangle(x0, y0, x1, y1, fill=color)
            return 1

        elif gamepiece == gamePiece._ghost_house:
            x0 = i * size
            y0 = j * size
            x1 = x0 + size
            y1 = y0 + size
            self._canvas.create_rectangle(x0, y0, x1, y1, fill=color)
            return 1
        elif gamepiece == gamePiece._ghost:
            x0 = i * size
            y0 = j * size
            x1 = x0 + size
            y1 = y0 + size
            self._canvas.create_rectangle(x0, y0, x1, y1, fill=color)
            return 1
        else:
            return 0
        
    def _display_pacman_position_text(self, pacman_row_position, pacman_column_position, pacman_state):

        #title
        self._label = Label(self._root, text = "Positions:",font=('Times', 24), bg= "white", fg = "black")
        self._label.grid(row=1, column=0)

        self._label = Label(self._root, text = "ROW",font=('Times', 24), bg= "white", fg = "black")
        self._label.grid(row=1, column=1)

        self._label = Label(self._root, text = "COLUMN",font=('Times', 24), bg= "white", fg = "black")
        self._label.grid(row=1, column=2)

        self._label = Label(self._root, text = "STATE",font=('Times', 24), bg= "white", fg = "black")
        self._label.grid(row=1, column=3)

        #----pacman
        self._label = Label(self._root, text = "Pac-man",font=('Times', 24), bg= "white", fg = "gold")
        self._label.grid(row=2, column=0)

        self._label = Label(self._root, text = pacman_row_position,font=('Times', 24), bg= "white", fg = "gold")
        self._label.grid(row=2, column=1)

        self._label = Label(self._root, text = pacman_column_position,font=('Times', 24), bg= "white", fg = "gold")
        self._label.grid(row=2, column=2)

        self._label = Label(self._root, text = pacman_state ,font=('Times', 24), bg= "white", fg = "gold")
        self._label.grid(row=2, column=3)

    def _display_ghost_position_text(self, ghost_obj):

        #local vars
        ghost_direction = ghost_obj._direction
        ghost_state = ghost_obj._state
        row_position = ghost_obj.row
        column_position = ghost_obj.col
        
        #----ghosts
        if ghost_obj._name == "Pinky":
            ghost_name = "Pinky"
            r = 3
            ghost_color = "pink"

        elif ghost_obj._name == "Blinky":
            ghost_name = "Blinky"
            r = 4
            ghost_color = "red"

        elif ghost_obj._name == "Clyde":
            ghost_name = "Clyde"
            r = 5
            ghost_color = "orange"

        elif ghost_obj._name == "Inky":
            ghost_name = "Inky"
            r = 6
            ghost_color = "cyan"
            
        #ghost
        self._label = Label(self._root, text = ghost_name,font=('Times', 24), bg= "white", fg = ghost_color)
        self._label.grid(row= r, column=0)

        self._label = Label(self._root, text = row_position,font=('Times', 24), bg= "white", fg = ghost_color)
        self._label.grid(row=r, column=1)

        self._label = Label(self._root, text = column_position,font=('Times', 24), bg= "white", fg = ghost_color)
        self._label.grid(row=r, column=2)

        self._label = Label(self._root, text = ghost_state ,font=('Times', 24), bg= "white", fg = ghost_color)
        self._label.grid(row=r, column=3)

        self._label = Label(self._root, text = ghost_direction ,font=('Times', 24), bg= "white", fg = ghost_color)
        self._label.grid(row=r, column=4)


    def _update_position_of_pacman(self, row, col):
        self._draw_shape(row, col, gamePiece._pacman) # draw pacman

        return 1
    
    def _update_position_of_ghost(self, ghost_obj):
        r = ghost_obj.row
        c = ghost_obj.col
        name = ghost_obj._name

        if name == "Blinky":
            self._draw_shape(r,c, gamePiece._ghost, ghost_obj)
        elif name == "Pinky":
            self._draw_shape(r,c, gamePiece._ghost, ghost_obj)
        elif name == "Inky":
            self._draw_shape(r,c, gamePiece._ghost, ghost_obj)
        elif name == "Clyde":
            self._draw_shape(r,c, gamePiece._ghost, ghost_obj)
        else:
            return 0

        return 1
    