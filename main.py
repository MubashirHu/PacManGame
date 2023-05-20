from view import *
from model import *
from controller import *

def main():
    
    my_controller = Controller()

    my_controller._initialize_game()
    my_controller._display_game()
    my_controller._execute()
    
    pass

if __name__ == "__main__":
    main()