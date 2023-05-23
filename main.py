from view import *
from model import *
from controller import *

def main():

    myController = Controller()

    myController._initialize_game()
    myController._display_game()
    myController._set_controls()
    myController.my_view._root.mainloop()
    
if __name__ == "__main__":
    main() 