#This file is the brain of the file and relays information to and from the model.py and view.py
from model import *
from view import *
class Controller:
    def __init__(self):
        self.my_model = Model()
        self.my_view = View()

    def _initialize_game(self):
        if self.my_model._initialize():
            self.my_view._initialize()
            print("Both view and model have been initialized...")

    def _display_game(self):
        for i in range(self.my_model.Map._rows):
            for j in range(self.my_model.Map._columns):
                _coordinates_of_path_and_wall = self.my_model._check_for_walls_and_path(i, j)       
                self.my_view._draw_shape(_coordinates_of_path_and_wall[0], _coordinates_of_path_and_wall[1], _coordinates_of_path_and_wall[2])

    def _execute(self):
        self.my_view._root.mainloop()     
                

    