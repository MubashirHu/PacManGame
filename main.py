from view import *
from model import *
from controller import *

def main():
    
    my_controller = Controller()

    my_controller._initialize_game()
    my_controller._display_game()
    my_controller._set_controls()
    my_controller.my_view._root.mainloop()
    
if __name__ == "__main__":
    main()