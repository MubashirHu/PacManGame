from view import *
from model import *
from controller import *
import threading

def main():

    myController = Controller()
    myController._initialize_model_and_view()

    myController.my_view._root.mainloop()
    
if __name__ == "__main__":
    main() 
