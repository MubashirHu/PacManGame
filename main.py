from view import *
from model import *
from controller import *
import threading

def main():

    myController = Controller()
    myController._initialize_game()
    myController._display_initial_positions()
    myController._set_initial_states_and_ghost_targets()
    myController._display_positions_of_pieces_in_view_text()

    myController.my_view._root.mainloop()
    
if __name__ == "__main__":
    main() 
