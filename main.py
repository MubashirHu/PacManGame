from view import *
from model import *
from controller import *
import threading

def main():

    myController = Controller()
    myController._initialize_model_and_view()
    myController._display_initial_positions()
    myController._display_coordinates()

    myController.my_view._root.mainloop()
    
if __name__ == "__main__":
    main() 
